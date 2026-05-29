#!/usr/bin/env python3
"""ASDF Stage-1 deterministic static security scanner.

A READ-ONLY, deterministic, reproducible pattern + structure scan of a Claude
skill / MCP / tool repository. It is the runnable heart of the Academic Skill
Analysis Framework (ASDF). It implements:

  - the pattern rules in `rules/patterns.yml`              (content regexes)
  - the structural checks in `rules/structural_checks.md`  (license/hooks/tools/deps)
  - a 4-band severity model whose names are anchored to CVSS/OpenSSF
    conventions (no CVSS vector is computed; see ../SEVERITY.md)
  - a Stage-0 (author declaration) vs Stage-1 (inferred) cross-check -> Discrepancies

Design principles (from the framework's trust factors):
  * OPEN          — every rule is readable data in rules/ ; the regex IS the doc.
  * DETERMINISTIC — same repo + same rule version -> same findings, every run.
  * READ-ONLY     — never executes repo code, installs nothing, only reads files.
  * HONEST        — a clean scan is NOT proof of safety; grep/AST is evadable.
                    This produces TRIAGE EVIDENCE, not a verdict. See ../README.md.
  * BOUNDED       — Stage 1 does the falsifiable, mechanical part only. Subjective
                    judgment (code quality, scope fit) is Stage 2 (evaluate-repository).

It never decides inclusion and NEVER exits non-zero on findings — only on a
usage / IO error (e.g. a clone that failed). Findings go to stdout (human) and,
with --json, to a machine-readable object a pipeline can consume.

Usage:
  python security_scan.py <path-to-repo>                 # scan a local clone
  python security_scan.py --repo <clone_url>             # shallow-clone + scan
  python security_scan.py <path> --declared decl.json    # cross-check a Stage-0 block
  python security_scan.py <path> --json                  # emit machine-readable JSON
  python security_scan.py --self-test                    # scan this list's own repo

Dependencies: PyYAML (already a project dependency; used to read the rule data).
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile

try:
    import yaml  # PyYAML — already a project dep (generator + schema use it)
except ImportError:  # pragma: no cover - explicit, honest failure
    sys.stderr.write(
        "security_scan: PyYAML is required to read the rule data. "
        "Install with `pip install pyyaml`.\n"
    )
    raise

# --------------------------------------------------------------------------
# Severity bands — NAMES anchored to CVSS v3.1 qualitative bands + OpenSSF risk
# levels (no CVSS vector is computed). Ordered most-severe first. See
# ../SEVERITY.md for the full rubric.
# --------------------------------------------------------------------------
CRITICAL = "Critical"
HIGH = "High"
MEDIUM = "Medium"
LOW = "Low"
INFO = "Info"  # positive / context only — never gates a label

_BAND_ORDER = {CRITICAL: 0, HIGH: 1, MEDIUM: 2, LOW: 3, INFO: 4}

# Files we actually read (skip binaries, vendored deps, VCS).
_TEXT_EXT = {
    ".md", ".markdown", ".txt", ".py", ".js", ".ts", ".tsx", ".jsx", ".mjs",
    ".cjs", ".sh", ".bash", ".zsh", ".ps1", ".rb", ".pl", ".php", ".lua",
    ".yaml", ".yml", ".json", ".toml", ".cfg", ".ini", ".env", ".rs", ".go",
    ".java", ".kt", ".c", ".cpp", ".h", ".hpp", ".r", ".jl", ".tex",
}
_ALWAYS_READ = {"SKILL.md", "settings.json", "settings.local.json", "LICENSE",
                "Dockerfile", "Makefile", ".env", "plugin.json",
                "marketplace.json", "requirements.txt", "package.json",
                "pyproject.toml"}
_SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "env", "dist", "build",
              "__pycache__", ".mypy_cache", ".pytest_cache", ".ruff_cache",
              "vendor", "target", ".next", ".idea", ".vscode", "site-packages"}
_MAX_BYTES = 2_000_000  # skip files larger than ~2 MB (likely data / binaries)

# Network-IO signature used to (a) escalate a hook that also calls the network
# and (b) infer makes_network_calls for the Stage-0 cross-check. Deliberately
# excludes socket.AF_UNIX (local IPC, e.g. LibreOffice control) — handled below.
_NETWORK_RX = re.compile(
    r"\b(requests\.(get|post|put|patch|delete|request)|urllib\.request|urlopen"
    r"|http\.client|httpx\.|aiohttp\.|socket\.socket|fetch\(|axios\.|XMLHttpRequest"
    r"|curl\s|wget\s|Invoke-WebRequest|net/http|reqwest::)",
    re.IGNORECASE,
)
# A socket that is explicitly AF_UNIX is local IPC, not network egress — do not
# count it as a network call (common FP: LibreOffice/soffice control sockets).
_AF_UNIX_RX = re.compile(r"AF_UNIX")
# allowed-tools Bash wildcard / unscoped Bash.
_BASH_WILDCARD = re.compile(
    r"Bash\s*\(\s*\*\s*\)|allowed[-_]tools\s*:\s*\[?[^\]\n]*\bBash\b(?!\s*\()",
    re.IGNORECASE,
)
# bare-public-ip is suppressed entirely in these file kinds: dependency manifests
# (version pins look like IPs) and recorded HTTP test cassettes / stub data
# (cookie tokens and page fragments produce torrents of false positives).
_IP_SKIP_SUFFIXES = (
    "requirements.txt", "pyproject.toml", "package.json", "package-lock.json",
    "poetry.lock", "pnpm-lock.yaml", "yarn.lock", "cargo.toml", "cargo.lock",
    "go.mod", "go.sum", "uv.lock", "pdm.lock", "gemfile.lock",
)
_IP_SKIP_DIR_HINTS = ("/cassettes/", "/stub_data/", "/fixtures/", "/__snapshots__/",
                      "/vcr/", "/test_data/", "/testdata/")

# Findings of the "scary" categories are DOWNGRADED one band (recorded) when they
# occur in a test/fixture or a security-tooling context — because that is where a
# legitimate skill *deliberately* contains the strings of the attacks it tests or
# blocks (a path-traversal test asserting `../etc/passwd` is rejected; a guard
# enumerating `.aws/credentials` to defend it; a reverse-shell signature in a
# detector's own rule list). The finding is still surfaced — never dropped — so a
# human can confirm it really is defensive. Scripts that actually DO the dangerous
# thing in non-test, non-guard code keep full severity.
_SECURITY_CTX_CATEGORIES = {"credential-path-read", "reverse-shell", "decode-then-exec",
                            "destructive-command", "exfil-webhook", "exfil-data-read",
                            "shell-exec-spawn", "dangerous-powershell"}
_SECURITY_CTX_FILE_HINTS = ("/test", "test_", "_test", "/tests/", "/spec", "conftest",
                            "/fixtures/", "/cassettes/", "/__snapshots__/",
                            "/security", "security-", "guard", "validator", "audit",
                            "boundary", "hotpatch", "sanitiz", "/.github/",
                            # A skill's OWN scanner / denylist file deliberately enumerates
                            # the attack signatures it blocks (a `threat_scan.py`/`detect.py`
                            # listing `.netrc`/`reverse-shell`/`mimikatz` to REJECT them is
                            # defensive, not malicious). Always recorded; never dropped.
                            "threat_scan", "threatscan", "/detect", "detect.", "denylist",
                            "deny_list", "blocklist", "block_list", "/scanner", "scan_",
                            "_scan", "patterns.yml", "signature", "/rules/")
# Denylist/scanner-tool files get a DEEP (two-band) downgrade for the scary categories:
# an attack string in a detector's own rule list is as benign as one in textbook prose.
_DENYLIST_CTX_HINTS = ("threat_scan", "threatscan", "/detect", "detect.", "denylist",
                       "deny_list", "blocklist", "block_list", "/scanner", "patterns.yml",
                       "signature", "/rules/")

# Documentation / example-data files: a dangerous string here is text being
# SHOWN (textbook prose, an example dataset, a sample document) rather than code
# the skill executes. For the high-impact "scary" categories these get a DEEP
# (two-band) downgrade so a `/etc/passwd` string inside Think-Python textbook
# prose cannot land at High (R4 F-1). Other categories get the normal one-band
# doc downgrade. Both are always recorded, never silently dropped.
_DEEP_DOWNGRADE_CATEGORIES = {"credential-path-read", "destructive-command",
                              "exfil-webhook", "exfil-data-read", "reverse-shell",
                              "decode-then-exec", "dangerous-powershell"}
# Categories where a match on a COMMENTED-OUT code line is a false positive
# (commented code is not executed). Doc/example prose is handled by the context
# downgrade; this targets commented code inside real scripts.
_COMMENT_SKIP_CATEGORIES = {"dangerous-eval-exec", "shell-exec-spawn",
                            "destructive-command", "reverse-shell",
                            "decode-then-exec", "dangerous-powershell"}
# path hints that mark a file as example-data / sample content (not executable code)
_EXAMPLE_DATA_DIR_HINTS = ("/examples/", "/example/", "/sample", "/samples/",
                           "/data/examples/", "/demo/", "/demos/", "/fixtures/",
                           "/testdata/", "/test_data/", "/corpus/", "/golden/",
                           "/__snapshots__/", "/cassettes/", "/templates/")
_DOC_EXTS = {".md", ".markdown", ".txt", ".rst"}


# --------------------------------------------------------------------------
def _here() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def load_rules(rules_path: str | None = None) -> tuple[list, str]:
    """Load and compile pattern rules from rules/patterns.yml.

    Returns (compiled_rules, rules_version). compiled_rules is a list of dicts:
    {id, category, severity, regex(compiled), message, note}.
    """
    if rules_path is None:
        rules_path = os.path.join(_here(), "rules", "patterns.yml")
    with open(rules_path, "r", encoding="utf-8") as fh:
        raw = fh.read()
    data = yaml.safe_load(raw) or {}
    rules = []
    for r in data.get("rules", []):
        sev = r["severity"]
        if sev not in (CRITICAL, HIGH, MEDIUM, LOW):
            raise ValueError(f"rule {r.get('id')!r}: bad severity {sev!r}")
        rules.append({
            "id": r["id"],
            "category": r.get("category", r["id"]),
            "severity": sev,
            "regex": re.compile(r["regex"], re.IGNORECASE),
            "message": r.get("message", ""),
            "note": r.get("note", ""),
        })
    # rules_version: a short content hash so a report can record exactly which
    # rule snapshot produced it (reproducibility / provenance, factor A7).
    import hashlib
    rules_version = hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]
    return rules, rules_version


def _within(root_real: str, path: str) -> bool:
    """True iff `path`'s real (symlink-resolved) location is inside `root_real`.

    The safety precondition for a read-only scanner: never read a file whose
    real target escapes the clone (a symlink pointing at /etc/passwd, ~/.ssh,
    or any absolute path outside the repo). os.path.realpath collapses the
    symlink chain; we then require the result to be under root_real.
    """
    try:
        rp = os.path.realpath(path)
    except OSError:
        return False
    # normcase for case-insensitive filesystems; ensure a path-separator boundary
    rp_n = os.path.normcase(rp)
    root_n = os.path.normcase(root_real)
    return rp_n == root_n or rp_n.startswith(root_n + os.sep)


def iter_text_files(root: str):
    # Symlink guard: resolve the clone root once, then refuse to descend into
    # symlinked directories or read symlinked files, and refuse to read any file
    # whose real path escapes the clone. A symlink is never followed — this keeps
    # the scan strictly inside the repository and prevents reading sensitive
    # local files (e.g. a `creds -> ~/.aws/credentials` symlink committed to a repo).
    root_real = os.path.realpath(root)
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        # prune skip-dirs AND symlinked subdirectories (do not descend into them)
        dirnames[:] = [d for d in dirnames
                       if d not in _SKIP_DIRS
                       and not os.path.islink(os.path.join(dirpath, d))]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            path = os.path.join(dirpath, fn)
            if ext not in _TEXT_EXT and fn not in _ALWAYS_READ:
                continue
            # never read a symlinked file, and never read outside the clone
            if os.path.islink(path) or not _within(root_real, path):
                continue
            try:
                if os.path.getsize(path) > _MAX_BYTES:
                    continue
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    yield path, fh.read()
            except (OSError, UnicodeError):
                continue


def rel(root: str, path: str) -> str:
    return os.path.relpath(path, root)


def _downgrade(sev: str, bands: int = 1) -> str:
    """`bands` steps less severe (clamped to Low). Used for context downgrades
    in documentation / example-data / test / security-tooling files."""
    chain = [CRITICAL, HIGH, MEDIUM, LOW]
    i = chain.index(sev)
    return chain[min(i + bands, len(chain) - 1)]


class Finding:
    __slots__ = ("severity", "category", "file", "line", "snippet", "note",
                 "downgraded_from", "downgrade_reason")

    def __init__(self, severity, category, file, line, snippet, note="", downgraded_from=None):
        self.severity = severity
        self.category = category
        self.file = file
        self.line = line
        self.snippet = snippet
        self.note = note
        self.downgraded_from = downgraded_from
        self.downgrade_reason = None

    def as_dict(self):
        d = {"severity": self.severity, "category": self.category,
             "file": self.file, "line": self.line, "snippet": self.snippet}
        if self.note:
            d["note"] = self.note
        if self.downgraded_from:
            d["downgraded_from"] = self.downgraded_from
            d["downgrade_reason"] = self.downgrade_reason or "context"
        return d


def scan_repo(root: str, rules: list) -> dict:
    findings: list[Finding] = []
    has_license = False
    hook_files: list[str] = []
    has_deny_rules = False
    allowed_tools_wildcard = False
    files_scanned = 0
    # inferred capability for the Stage-0 cross-check
    inferred = {
        "makes_network_calls": False,
        "has_hooks": False,
        "network_endpoints": set(),
        "telemetry": False,
        "allowed_tools_wildcard": False,  # set when Bash(*)/unscoped Bash is seen
    }

    for path, text in iter_text_files(root):
        files_scanned += 1
        name = os.path.basename(path)
        relpath = rel(root, path)
        relposix = relpath.replace("\\", "/")
        # Documentation files (markdown/text/rst): a dangerous *pattern* here is
        # almost always a command being DOCUMENTED (install/uninstall steps, a
        # "blocked example", a syntax table) rather than code the skill RUNS. We
        # downgrade findings in these files one band, reason recorded — never
        # silently dropped. Scripts (.py/.sh/.ps1/...) keep full severity.
        is_doc = os.path.splitext(name)[1].lower() in {".md", ".markdown", ".txt", ".rst"}
        lines = text.splitlines()

        # structural: license
        if name in {"LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING",
                    "COPYING.md", "UNLICENSE"} or re.match(r"(?i)licen[sc]e", name):
            has_license = True

        lower = text.lower()
        # structural: hooks — ONLY genuine Claude/agent lifecycle hooks, never a
        # React/frontend custom-hook directory (`src/hooks/`, `app/hooks/`, a
        # `useFoo.ts` file). A real lifecycle hook is declared as a `hooks:` /
        # `"hooks":` key in a skill/agent config (SKILL.md frontmatter,
        # settings.json, plugin/marketplace manifest) OR lives under an
        # agent-config hooks dir (`.claude/hooks/`, `.agent/hooks/`, a top-level
        # `hooks/` that is NOT under a frontend source root).
        relposix_path = "/" + relposix
        # a `hooks:`/`"hooks":` key in a recognised agent-config file
        _hook_config_file = name in {"SKILL.md", "settings.json", "settings.local.json",
                                     "plugin.json", "marketplace.json", "config.yaml",
                                     "config.yml", "agent.json", "agent.yaml", "agent.yml"}
        _has_hook_key = bool(re.search(r'(^|\n)\s*"?hooks"?\s*:', text))
        # an agent-config hooks directory (explicitly excludes frontend source dirs)
        _FRONTEND_ROOTS = ("/src/hooks/", "/app/hooks/", "/lib/hooks/",
                           "/components/hooks/", "/packages/", "/frontend/",
                           "/client/", "/web/", "/ui/hooks/", "/renderer/")
        _in_agent_hooks_dir = (
            ("/.claude/hooks/" in relposix_path or "/.agent/hooks/" in relposix_path
             or "/.codex/hooks/" in relposix_path)
            or (("/hooks/" in relposix_path or relposix_path.startswith("/hooks/"))
                and not any(fr in relposix_path for fr in _FRONTEND_ROOTS))
        )
        is_hook_file = (_hook_config_file and _has_hook_key) or _in_agent_hooks_dir
        if is_hook_file:
            hook_files.append(relpath)
            inferred["has_hooks"] = True
            # escalate: a hook file that also makes network calls
            if _NETWORK_RX.search(text):
                findings.append(Finding(
                    HIGH, "hook-network-io", relpath, 0,
                    "Hook/lifecycle file also performs network IO — silent auto-run + network.",
                    note="A hook runs automatically on lifecycle events; combined with network "
                         "IO this is implicit data egress with no user action. Mandatory manual review.",
                ))

        # structural: deny rules (positive), allowed-tools wildcard
        if re.search(r'"deny"\s*:|(^|\n)\s*deny\s*:', text):
            has_deny_rules = True
        if _BASH_WILDCARD.search(text):
            allowed_tools_wildcard = True

        # inferred network capability (for the Stage-0 cross-check). A match that
        # is ONLY a socket.socket(AF_UNIX,...) is local IPC, not network egress.
        net_match = _NETWORK_RX.search(text)
        if net_match:
            only_unix = (net_match.group(0).startswith("socket.socket")
                         and _AF_UNIX_RX.search(text)
                         and not re.search(r"socket\.socket\([^)]*AF_INET", text))
            # if the file's only network signature is socket.socket and it is
            # AF_UNIX, don't count it; otherwise (or if other sigs present) count.
            sigs = set(m.group(0).split("(")[0] for m in _NETWORK_RX.finditer(text))
            non_socket_sigs = sigs - {"socket.socket"}
            if non_socket_sigs or not only_unix:
                inferred["makes_network_calls"] = True
        for m in re.finditer(r"https?://([A-Za-z0-9.\-]+)", text):
            host = m.group(1).lower()
            # ignore docs/badges/non-runtime hosts AND XML-namespace schema URIs
            # (OOXML/ODF declare schemas.microsoft.com / openxmlformats.org etc.
            # as namespace identifiers — they are never fetched).
            if not any(host.endswith(s) or host == s for s in (
                "github.com", "githubusercontent.com", "shields.io", "img.shields.io",
                "anthropic.com", "claude.ai", "example.com", "localhost",
                "schema.org", "json-schema.org", "spdx.org", "creativecommons.org",
                "w3.org", "opensource.org", "python.org", "npmjs.com", "mozilla.org",
                "apache.org", "gnu.org", "openxmlformats.org", "schemas.microsoft.com",
                "schemas.openxmlformats.org", "purl.org", "openoffice.org",
                "docbook.org", "oasis-open.org", "iso.org", "unicode.org",
            )):
                inferred["network_endpoints"].add(host)

        # bare-public-ip is suppressed wholesale in manifests + recorded cassettes
        relposix_l = ("/" + relposix).lower()
        skip_ip_here = (relposix_l.endswith(_IP_SKIP_SUFFIXES)
                        or any(h in relposix_l for h in _IP_SKIP_DIR_HINTS))
        # is this a test/fixture or security-tooling file?
        is_security_ctx = any(h in relposix_l for h in _SECURITY_CTX_FILE_HINTS)
        # is this specifically a denylist/scanner-tool file (deep downgrade)?
        is_denylist_ctx = any(h in relposix_l for h in _DENYLIST_CTX_HINTS)
        # is this an example-data / sample-content file (not executable code)?
        is_example_data = any(h in relposix_l for h in _EXAMPLE_DATA_DIR_HINTS)

        # pattern rules
        for rule in rules:
            if rule["id"] == "bare-public-ip" and skip_ip_here:
                continue
            cat = rule["category"]
            for m in rule["regex"].finditer(text):
                # Line number from the FIRST non-newline char of the match. Many
                # rules use a `(^|[^.\w])` prefix that can capture the preceding
                # `\n`; counting newlines up to a match that *starts on* that
                # `\n` would mis-attribute the finding to the previous line. Skip
                # any leading newlines in the match before computing the line.
                start = m.start()
                while start < len(text) and text[start] == "\n":
                    start += 1
                line_no = text.count("\n", 0, start) + 1
                raw_line = lines[line_no - 1] if 0 <= line_no - 1 < len(lines) else m.group(0)
                snippet = raw_line.strip()[:140]
                stripped = raw_line.lstrip()

                # F-2: an execution/destructive pattern on a COMMENTED-OUT line
                # (`# os.system(...)`, `// eval(...)`, `* exec(...)` in a block
                # comment, `<!-- ... -->`) is not a live sink — skip it for the
                # execution/destructive categories. (Doc/example prose is handled
                # separately by the context downgrade; this is for commented code
                # inside scripts.)
                if cat in _COMMENT_SKIP_CATEGORIES and (
                        stripped.startswith("#") or stripped.startswith("//")
                        or stripped.startswith("*") or stripped.startswith("<!--")):
                    continue
                # F-2: dangerous-eval-exec must not fire on a function/method
                # DEFINITION or a class named Eval/Exec (`def eval(`, `async def
                # eval(`, `class Eval(`, `def exec(`). A definition is not an
                # execution sink — it is the thing being defined.
                if rule["id"] == "dangerous-eval-exec" and re.match(
                        r'(async\s+)?def\s+(eval|exec)\b|class\s+(Eval|Exec)\b', stripped):
                    continue

                sev = rule["severity"]
                downgraded_from = None
                reason = None
                # Context downgrades (recorded, never silent). Precedence:
                #   1. doc / example-data:
                #        - deep (two-band) for high-impact "scary" categories — a
                #          credential/destructive/exfil/shell string in textbook
                #          prose or an example dataset is virtually never live code
                #          (R4 F-1: /etc/passwd in Think-Python prose must not be High);
                #        - one-band for everything else.
                #   2. else test / security-tooling context: one-band for the
                #      scary categories (a guard/test legitimately contains the
                #      strings of the attacks it blocks/asserts).
                # We never apply more than one downgrade reason.
                if (is_doc or is_example_data) and sev != LOW:
                    if cat in _DEEP_DOWNGRADE_CATEGORIES:
                        downgraded_from = sev
                        sev = _downgrade(sev, 2)
                        reason = "example-data" if (is_example_data and not is_doc) else "doc"
                    else:
                        downgraded_from = sev
                        sev = _downgrade(sev, 1)
                        reason = "example-data" if (is_example_data and not is_doc) else "doc"
                elif (is_security_ctx and sev != LOW
                      and cat in _SECURITY_CTX_CATEGORIES):
                    downgraded_from = sev
                    # A denylist/scanner file enumerating attack signatures to BLOCK
                    # them is as benign as textbook prose -> deep (two-band) downgrade;
                    # an ordinary test/guard file keeps the one-band downgrade.
                    sev = _downgrade(sev, 2 if is_denylist_ctx else 1)
                    reason = "denylist/scanner-tool" if is_denylist_ctx else "test/security-context"

                # F-4: hidden-unicode inside a NAMED quoted string literal is a
                # deliberate feature (e.g. `zwsp_char = "<ZWSP>" if zwsp else ""`),
                # not a Trojan-Source attack (which hides the char inside an
                # identifier or a bare instruction). Down-weight to Low + note.
                if rule["id"] == "hidden-unicode" and sev != LOW:
                    if re.search(r'^[A-Za-z_][\w\.]*\s*[:=]\s*[a-z]*["\']', stripped) \
                            or re.match(r'^["\']', stripped):
                        downgraded_from = downgraded_from or sev
                        sev = LOW
                        reason = "named-string-literal (deliberate ZWSP feature, not Trojan-Source)"

                # telemetry inference for the cross-check
                if rule["id"] == "telemetry-endpoint":
                    inferred["telemetry"] = True
                f = Finding(sev, cat, relpath, line_no, snippet,
                            note=rule["note"], downgraded_from=downgraded_from)
                f.downgrade_reason = reason
                findings.append(f)

    # ---- structural findings (presence/config) -------------------------------
    if not has_license:
        findings.append(Finding(
            MEDIUM, "license-missing", "(repo root)", 0,
            "No LICENSE / COPYING file found — license must be stated for safe reuse."))
    if allowed_tools_wildcard:
        # MEDIUM, not High: for an INDEX this is a disclosure/scope flag, not evidence of
        # a threat — a great many legitimate skills ship `Bash(*)` (like the official-installer
        # `curl|sh`, it's "disclose, don't disqualify"). The declared-vs-inferred discrepancy
        # below still fires at High if an author CLAIMS scoped tools but ships a wildcard
        # (under-disclosure), which is the genuinely trust-relevant case.
        findings.append(Finding(
            MEDIUM, "allowed-tools-wildcard", "(SKILL.md / settings)", 0,
            "Bash(*) or unscoped Bash in allowed-tools — unrestricted shell; should be scoped.",
            note="The widest execution surface; common but worth scoping, e.g. Bash(git:*). "
                 "Medium (disclose-not-disqualify); an UNDISCLOSED wildcard is flagged High below."))
    if hook_files:
        findings.append(Finding(
            MEDIUM, "hooks-present", ", ".join(sorted(set(hook_files))[:5]) or "(hooks)", 0,
            "Hook/lifecycle execution present — runs implicitly on tool events; enumerate triggers.",
            note="Implicit execution the user did not directly invoke. Any network IO in a hook escalates to High."))

    # positives (context only; never gate a label)
    if has_license:
        findings.append(Finding(INFO, "license-present", "(repo root)", 0, "License file present."))
    if has_deny_rules:
        findings.append(Finding(INFO, "deny-rules-present", "(settings)", 0,
                                "Explicit deny rules found — positive defensive signal."))

    inferred["network_endpoints"] = sorted(inferred["network_endpoints"])
    inferred["allowed_tools_wildcard"] = allowed_tools_wildcard
    return {
        "root": root,
        "files_scanned": files_scanned,
        "findings": findings,
        "inferred": inferred,
        "has_license": has_license,
    }


def cross_check(declared: dict | None, inferred: dict) -> list[dict]:
    """Stage-0 (author declaration) vs Stage-1 (inferred) -> Discrepancies.

    A discrepancy is a place where the author's claim disagrees with what the
    static scan inferred. A FALSE declaration caught here is a strong reject
    signal (factor A6) — a verifiable, non-subjective trust judgment.
    Each item: {field, declared, inferred, severity, note}.
    """
    if not declared:
        return []
    disc = []
    # network: declared false but calls inferred -> High (under-disclosure)
    dn = declared.get("makes_network_calls")
    if dn is False and inferred.get("makes_network_calls"):
        disc.append({
            "field": "makes_network_calls", "declared": False, "inferred": True,
            "severity": HIGH,
            "note": "Author declares no network calls, but the scan found network IO. "
                    "Under-disclosure of a network capability — verify before trusting.",
            "evidence": inferred.get("network_endpoints", []),
        })
    # hooks: declared false but hooks found -> High (undisclosed implicit exec)
    dh = declared.get("has_hooks")
    if dh is False and inferred.get("has_hooks"):
        disc.append({
            "field": "has_hooks", "declared": False, "inferred": True,
            "severity": HIGH,
            "note": "Author declares no hooks, but a hook/lifecycle declaration was found. "
                    "Undisclosed implicit execution surface.",
        })
    # telemetry: declared false but telemetry endpoint found -> Medium
    dt = declared.get("telemetry")
    if dt is False and inferred.get("telemetry"):
        disc.append({
            "field": "telemetry", "declared": False, "inferred": True,
            "severity": MEDIUM,
            "note": "Author declares no telemetry, but an analytics/telemetry endpoint was found.",
        })
    # allowed-tools scope: declared scoped (true) but an unscoped Bash / Bash(*)
    # was inferred -> High (a false "we scoped the tools" declaration). This is
    # the textbook declared-vs-inferred catch (R4 F-3) and it fires on the
    # owner's own paper-search-pro, which declares allowed_tools_scoped: true yet
    # ships a bare `Bash` — neutrality caught by construction, not by goodwill.
    ds = declared.get("allowed_tools_scoped")
    if ds is True and inferred.get("allowed_tools_wildcard"):
        disc.append({
            "field": "allowed_tools_scoped", "declared": True, "inferred": False,
            "severity": HIGH,
            "note": "Author declares the tool allowlist is scoped, but the scan found "
                    "`Bash(*)` or a bare unscoped `Bash` — the widest execution surface. "
                    "A false scope declaration; the Bash permission should be narrowed "
                    "(e.g. Bash(git:*)) or the declaration corrected.",
        })
    # endpoint set: declared endpoints that omit inferred hosts -> Low (info)
    declared_eps = set(e.lower() for e in (declared.get("network_endpoints") or [])
                       if isinstance(e, str))
    inferred_eps = set(inferred.get("network_endpoints", []))
    # only flag inferred hosts not covered by any declared endpoint substring
    uncovered = sorted(h for h in inferred_eps
                       if not any(h in d or d in h for d in declared_eps))
    if declared_eps and uncovered:
        disc.append({
            "field": "network_endpoints", "declared": sorted(declared_eps),
            "inferred": sorted(inferred_eps), "severity": LOW,
            "note": "Static scan saw host(s) not in the declared endpoint list "
                    "(may be docs/examples; verify): " + ", ".join(uncovered[:8]),
        })
    return disc


def top_band(findings: list[Finding], discrepancies: list[dict]) -> str:
    """The most-severe band across findings + discrepancies (Info ignored)."""
    bands = [f.severity for f in findings if f.severity != INFO]
    bands += [d["severity"] for d in discrepancies]
    if not bands:
        return LOW  # nothing above Info -> treat as Low (clean-ish) baseline
    return min(bands, key=lambda b: _BAND_ORDER.get(b, 99))


# A band -> analyzed/listed `label_for()` lived here until v1.1; the published
# verdict was dropped for the disclosure model. The scan now reports the band only
# as advisory triage (see print_report) — capability facts, not a label.
# --------------------------------------------------------------------------
def count_bands(findings):
    c = {CRITICAL: 0, HIGH: 0, MEDIUM: 0, LOW: 0, INFO: 0}
    for f in findings:
        c[f.severity] = c.get(f.severity, 0) + 1
    return c


def sort_findings(findings):
    return sorted(findings, key=lambda f: (_BAND_ORDER.get(f.severity, 99),
                                           f.category, f.file, f.line))


def print_report(result: dict, declared=None, discrepancies=None) -> str:
    findings = result["findings"]
    discrepancies = discrepancies or []
    counts = count_bands(findings)
    band = top_band(findings, discrepancies)
    out = []
    out.append("## ASDF Stage-1 deterministic static scan")
    out.append("")
    out.append(f"- Repo: `{result['root']}`")
    sha = git_commit_sha(result["root"])
    if sha:
        out.append(f"- Scanned commit: `{sha}`")
    out.append(f"- Files scanned: {result['files_scanned']}")
    out.append("- Findings: "
               + ", ".join(f"{counts[b]} {b}" for b in (CRITICAL, HIGH, MEDIUM, LOW)))
    out.append(f"- Top severity band: **{band}**")
    out.append("")
    out.append("> Best-effort static scan — triage evidence, not a verdict and not a "
               "safety guarantee. grep/AST checks are evadable; a clean scan is not "
               "proof of safety. A human curator decides inclusion. See framework/README.md.")
    out.append("")
    if discrepancies:
        out.append("### Discrepancies (declared vs inferred)")
        out.append("")
        out.append("| Field | Declared | Inferred | Severity | Note |")
        out.append("|---|---|---|---|---|")
        for d in discrepancies:
            note = str(d["note"]).replace("|", "\\|")
            out.append(f"| `{d['field']}` | {d['declared']} | {d['inferred']} | "
                       f"{d['severity']} | {note} |")
        out.append("")
    fs = sort_findings(findings)
    if fs:
        out.append("### Findings")
        out.append("")
        out.append("| Severity | Category | File | Line | Snippet |")
        out.append("|---|---|---|--:|---|")
        for f in fs:
            snip = (f.snippet or "").replace("|", "\\|").replace("`", "'")
            _dr = getattr(f, "downgrade_reason", None) or ""
            rtext = {"doc": "in a documentation file",
                     "example-data": "in an example-data file",
                     "test/security-context": "in a test / security-tooling context",
                     }.get(_dr, _dr or "context")
            extra = f" _(downgraded from {f.downgraded_from}: {rtext})_" if f.downgraded_from else ""
            out.append(f"| {f.severity} | {f.category}{extra} | `{f.file}` | {f.line or ''} | `{snip}` |")
    else:
        out.append("_No pattern findings._")
    out.append("")
    text = "\n".join(out)
    print(text)
    return text


def git_commit_sha(path: str) -> str | None:
    """Return the full HEAD commit SHA of the clone at `path`, or None.

    Recorded in each report so a scan is reproducible against an EXACT commit
    (R4/Codex reproducibility): "same repo + same rule version -> same findings"
    only means something if "same repo" is pinned to a commit, not a moving
    branch. Read-only: `git rev-parse HEAD` reads, never writes.
    """
    try:
        out = subprocess.run(
            ["git", "-C", path, "rev-parse", "HEAD"],
            check=True, capture_output=True, text=True, timeout=10).stdout.strip()
        return out or None
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        return None


def shallow_clone(clone_url: str) -> str:
    tmp = tempfile.mkdtemp(prefix="asaf_scan_")
    dest = os.path.join(tmp, "repo")
    subprocess.run(["git", "clone", "--depth", "1", "--quiet", clone_url, dest],
                   check=True)
    return dest


def run(root: str, declared: dict | None, rules_path: str | None = None) -> dict:
    """Programmatic entry: scan `root`, return a JSON-able result object."""
    rules, rules_version = load_rules(rules_path)
    result = scan_repo(root, rules)
    discrepancies = cross_check(declared, result["inferred"])
    band = top_band(result["findings"], discrepancies)
    return {
        "rules_version": rules_version,
        "commit_sha": git_commit_sha(root),
        "files_scanned": result["files_scanned"],
        "inferred": result["inferred"],
        "discrepancies": discrepancies,
        "top_severity": band,
        "counts": count_bands(result["findings"]),
        "findings": [f.as_dict() for f in sort_findings(result["findings"])],
    }


def main() -> int:
    ap = argparse.ArgumentParser(
        description="ASDF Stage-1 deterministic static security scanner (read-only, comment-only).")
    ap.add_argument("path", nargs="?", help="Path to a local repo clone to scan.")
    ap.add_argument("--repo", help="Clone URL to shallow-clone and scan (read-only).")
    ap.add_argument("--declared", help="Path to a JSON file of the entry's Stage-0 declared security block (for the cross-check).")
    ap.add_argument("--rules", help="Path to an alternate patterns.yml (default: rules/patterns.yml).")
    ap.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of the markdown report.")
    ap.add_argument("--self-test", action="store_true", help="Scan this list's own repo as a smoke test.")
    args = ap.parse_args()

    if args.self_test:
        root = os.path.normpath(os.path.join(_here(), "..", ".."))
    elif args.repo:
        try:
            root = shallow_clone(args.repo)
        except subprocess.CalledProcessError as e:
            print(f"security_scan: clone failed: {e}", file=sys.stderr)
            return 2
    elif args.path:
        root = args.path
    else:
        ap.print_help()
        return 2

    if not os.path.isdir(root):
        print(f"security_scan: not a directory: {root}", file=sys.stderr)
        return 2

    declared = None
    if args.declared:
        with open(args.declared, "r", encoding="utf-8") as fh:
            declared = json.load(fh)

    if args.json:
        print(json.dumps(run(root, declared, args.rules), indent=2, ensure_ascii=False))
    else:
        rules, _ = load_rules(args.rules)
        result = scan_repo(root, rules)
        discrepancies = cross_check(declared, result["inferred"])
        print_report(result, declared, discrepancies)

    # CONTRACT: never exit non-zero on findings — this is triage, not a gate.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
