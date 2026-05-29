# ASDF changelog

The framework carries a version so each scan records *which version* produced it
and *when* — a disclosure is only meaningful with "checked by what, when."
Versioning lets the framework evolve without silently invalidating earlier scans.

The format follows [Keep a Changelog](https://keepachangelog.com/); this project
versions the **disclosure framework** independently of the list's content.

## [1.1] — 2026-06-01

Refounded to **disclosure-only**. The static `analyzed` / `listed` severity verdict
was **removed**: on a 200+ repo run it produced too many false positives to trust
(four-part version strings read as IP addresses, a security tool's own block-list
read as an attack, a UI placeholder read as a destructive command). The framework
now publishes each entry's **disclosed capabilities** — network, hooks, permission
scope — cross-checked against the code, as facts rather than a safety rating.

### Changed
- Per-entry `analyzed` / `listed` label dropped. Entries carry capability tags
  (`net` / `hooks` / `bypass`) plus a `⚠ disclosure` flag when the author's
  declaration disagrees with the code.
- Severity bands retained only as an **advisory triage signal** inside the
  scanner's own output — they no longer drive any published label.
- Renamed *Academic Skill Analysis Framework* → **Academic Skill Disclosure
  Framework**; README / CRITERIA / SEVERITY reworded to match.

## [1.0] — 2026-05-29

First public version of the Academic Skill Disclosure Framework (ASDF). Replaces
the previous list's dishonest "human-reviewed / ✅ security-reviewed" badge with
an open, deterministic, reproducible, honestly-labeled analysis.

### Added
- **Methodology** ([README.md](README.md)) — the four-stage pipeline (author
  declaration → deterministic scan → bounded AI judgment → curator decision),
  the two honest labels (`analyzed` / `listed`), and an explicit **honest-limits**
  section ("static, best-effort, evadable; AI-analyzed not human-reviewed; listed
  ≠ unsafe; analyzed ≠ safe; you run third-party code at your own risk").
- **Criteria** ([CRITERIA.md](CRITERIA.md)) — every deterministic check and every
  subjective dimension, defined; the split between falsifiable code checks and
  bounded AI judgment made explicit.
- **Severity** ([SEVERITY.md](SEVERITY.md)) — a 4-band scale (Critical / High /
  Medium / Low) whose **names are anchored to** CVSS v3.1 bands and OpenSSF risk
  levels (no CVSS vector is computed), each band defined by finding-type.
- **Scanner** ([`scanner/security_scan.py`](scanner/security_scan.py)) — a
  runnable, read-only, deterministic Stage-1 scanner implementing the 13-category
  static scan plus structural checks (license, `Bash(*)`/unscoped-Bash wildcard,
  hooks, hook-network-IO escalation, unpinned deps) and the Stage-0-vs-Stage-1
  declared-vs-inferred **Discrepancies** cross-check. Emits markdown or `--json`.
  Never exits non-zero on findings (triage, not a gate).
- **Rules as readable data** ([`scanner/rules/patterns.yml`](scanner/rules/patterns.yml)
  + [`scanner/rules/structural_checks.md`](scanner/rules/structural_checks.md)) —
  semgrep-style open rules, each with a `message` and a false-positive `note`, so
  any heuristic can be read and contested.
- **Per-entry reports** ([`reports/`](reports/)) — one dated, framework-versioned
  report per listed entry: declared-vs-inferred, Discrepancies, findings by
  severity, a bounded conclusion, and a recusal note for owner-authored entries.
- **Analysis map** (`analysis.yml`) — the machine source the README generator
  renders into the per-entry label.
- **Validation record** ([VALIDATION.md](VALIDATION.md)) — the audit scope, the
  validation log (with the R4 expert audit pending before launch), author-declared
  known limitations, and the contest channel.

### Scanner false-positive calibration (build self-review, 2026-05-29)
Tuned against the full 89-entry run to keep labels honest and defensible:
- `bare-public-ip`: each octet must be 0–255 (so 4-part **version strings** like
  `1.27.2.3` no longer match as IPs); version operators (`==`, `>=`, `~=`, `^`)
  in the lookbehind; suppressed in dependency manifests and recorded HTTP test
  cassettes / fixture data.
- **Documentation-file downgrade**: a dangerous pattern in a `.md`/`.txt`/`.rst`
  file is downgraded one band (it is a command being *documented* — install /
  uninstall / a "blocked" example — not code the skill runs). Always recorded in
  the report; scripts keep full severity.
- `destructive-command`: matches **root / home / bare-wildcard** targets only
  (`rm -rf /tmp/foo` and `rm -rf ./build` are no longer flagged).
- Network inference: an `AF_UNIX` socket (local IPC, e.g. LibreOffice control) is
  **not** counted as a network call; XML-namespace schema URLs
  (`schemas.openxmlformats.org`, etc.) are **not** counted as fetched endpoints —
  fixing a false "under-declared network" discrepancy on the document skills.
- `dynamic-import-or-unpickle`: `__import__` (lazy import) and `pickle.loads`
  split out at **Medium** (a weaker signal than `eval`/`exec`).
- `suspicious-url`: `t.co/` now requires a left boundary so it no longer matches
  legitimate hosts ending in those strings (e.g. `posit.co`); `$eval` (Puppeteer
  DOM helper) excluded from `dangerous-eval-exec`.

### R4 audit fixes (FX1, 2026-05-29)
Applied after the R4 expert audit + an independent Codex cross-model review (full
record in [VALIDATION.md](VALIDATION.md)); the scanner was re-run over all 89
entries and `reports/*.md` + `analysis.yml` regenerated.
- **Scanner — false-negatives closed.** New rules `reverse-shell-py`
  (socket.connect + process-spawn across lines), `shell-exec-spawn`
  (`os.popen` / `child_process.exec` / bare `Popen(shell=True)`), and
  `exfil-data-read` (file-read-then-POST). Broadened `reverse-shell`
  (`nc host port -e …`, `socat … EXEC:`) and `decode-then-exec` (both orders +
  across a line break).
- **Scanner — safety + reproducibility.** Added a **symlink guard** (symlinks are
  never followed; files whose real path escapes the clone are refused) and
  recorded the **scanned commit SHA** in every report.
- **Scanner — precision.** Documentation *and* example-data files now downgrade
  credential/destructive/exfil/shell patterns **two bands** (a `/etc/passwd`
  string in textbook prose can no longer reach High); `dangerous-eval-exec` no
  longer fires on `def eval`/`class Eval`/commented code; **hook detection is
  scoped to genuine agent lifecycle hooks** (a `hooks:` config key or a
  `.claude/hooks/`-style dir) and no longer flags React/frontend `src/hooks/`
  paths or prose mentions of "hooks"; `hidden-unicode` in a named string literal
  (a deliberate ZWSP feature) is down-weighted to Low.
- **Scanner — new cross-check.** `allowed_tools_scoped: true` declared but an
  unscoped `Bash` inferred is now a **High** declared-vs-inferred discrepancy.
- **Honesty.** `SEVERITY.md` reworded (band names *anchored to* CVSS/OpenSSF, no
  vector computed). Report headers no longer claim "bounded AI judgment" for
  entries without an individual Stage-2. `ssci-plots`' ZWSP finding is described
  as the documented optional feature it is. Owner skills (`paper-search-pro`,
  `ssci-plots`) are recused → both `listed` pending independent review.

### Notes
- This is **AI-analyzed, not human-reviewed.** Stage 2 (subjective dimensions)
  was applied to a decision-relevant subset for this pass; the rest carry the
  deterministic Stage 0/1 plus an honest "available on demand" note.
- The R4 independent expert audit (criteria / scanner / severity / honesty /
  neutrality) — including an independent Codex cross-model review — **was completed
  on 2026-05-29** and is recorded in [VALIDATION.md](VALIDATION.md), along with the
  FX1 fixes above.

[1.0]: #10--20260529
