# ASDF criteria — every check and dimension, defined

This is the rubric, in the repo, versioned with the list. A reader can see
*exactly* what the framework checks and what each capability tag means. The
criteria split cleanly into two halves, on purpose:

- **Deterministic checks** (Part A) — a script runs them, they produce the same
  answer every run, anyone can re-run and verify them. These are *falsifiable*.
- **Subjective dimensions** (Part B) — they need judgment; an AI model scores
  them, labeled as AI, with explicit confidence. A skeptic verifies Part A
  mechanically and only has to weigh the model on Part B (which is disclosed).

Per the project's standing rule (*hard constraints before soft evaluation*): the
deterministic gates are evaluated first; the subjective dimensions are the soft
layer on top.

---

## Part A — Deterministic checks (Stage 1, the runnable scanner)

All of these are implemented in [`scanner/security_scan.py`](scanner/security_scan.py),
driven by readable rule data in [`scanner/rules/`](scanner/rules/). Each finding
carries a [severity band](SEVERITY.md). The 13 pattern categories below are the
core static scan; the structural checks follow.

### A.1 Content-pattern checks (`scanner/rules/patterns.yml`)

| # | Category | Band | What it looks for |
|--:|---|---|---|
| 1 | `reverse-shell` | Critical | interactive shell back to a remote host (`/dev/tcp/`, `nc -e`, `bash -i`, `socket.connect`, `pty.spawn`) |
| 2 | `decode-then-exec` | Critical | code hidden as an encoded blob then run (`base64 -d \| sh`, `b64decode(...)→exec`, `atob(...)→eval`) |
| 3 | `credential-path-read` | Critical | reads a secret path (`.ssh/id_*`, `.aws/credentials`, `/etc/shadow`, `.netrc`, `.git-credentials`, `.kube/config`) |
| 4 | `dangerous-powershell` | Critical | PowerShell dynamic-exec / download-and-run / encoded command (`IEX`, `DownloadString`, `FromBase64String`, `-EncodedCommand`) |
| 5 | `destructive-command` | Critical | recursive delete of **root/home/bare-wildcard**, fork bomb, raw disk write (`rm -rf /`, `rm -rf ~`, `chmod 777`, `dd … of=/dev/sd*`) |
| 6 | `exfil-webhook` | Critical | hard-coded chat/webhook exfil endpoint (Discord/Slack/Telegram webhooks, `webhook.site`, `requestbin`, `pipedream.net`) |
| 7 | `miner-or-rat` | Critical | cryptominer / RAT / offensive-tooling signature (`xmrig`, `stratum+tcp://`, `mimikatz`, `meterpreter`, `njrat`) |
| 8 | `dangerous-eval-exec` | High | dynamic code execution (`eval(`, `exec(`, `Function("…"`, unsafe `yaml.load`, `os.system(`, `subprocess(shell=True)`) |
| 9 | `suspicious-url` | High | URL shortener / paste-raw / tunnel / Tor (`bit.ly`, `pastebin.com/raw`, `ngrok`, `trycloudflare`, `.onion`) |
| 10 | `bare-public-ip` | High | a real, hard-coded public IPv4 (each octet 0–255; version strings and fixtures excluded) |
| 11 | `pipe-to-shell` | Medium | `curl … \| sh` install — runs unreviewed remote code (even official installers do this; flag-not-fail) |
| 12 | `auto-update-latest` | Medium | unpinned / auto-updating dependency (`@latest`, `pip install -U`, `cargo install --git`) |
| 13 | `dynamic-import-or-unpickle` | Medium | `__import__` (lazy import) or `pickle.loads` / `marshal.loads` (untrusted deserialization risk) |
| + | `long-base64-blob` | Medium | a ≥220-char base64 blob (could hide a payload, or just be an inlined asset — high FP, weak alone) |
| + | `prompt-injection` | Medium | "ignore previous instructions" / "developer mode" embedded in content |
| + | `jailbreak-marker` | Medium | fake `<system>` tag / "DAN mode" / "do anything now" |
| + | `hidden-unicode` | Medium | zero-width / RTL-override Unicode (Trojan-Source class) |
| + | `telemetry-endpoint` | Low | analytics/telemetry host (matters mainly as a declared-vs-inferred discrepancy) |

Each rule is open YAML with a `message` and a `note` documenting its rationale
and known false positives — read or contest them directly. The scanner applies
two recorded **context downgrades** (documentation files; version-string IPs in
manifests/fixtures) described in [SEVERITY.md](SEVERITY.md).

### A.2 Structural checks (`scanner/rules/structural_checks.md`)

| Check | Band of a negative result | What it inspects |
|---|---|---|
| `license-present` | Medium if missing (Info if present) | a `LICENSE` / `COPYING` at the repo root |
| `allowed-tools-wildcard` | High | `Bash(*)` or bare unscoped `Bash` in `allowed-tools` (unrestricted shell) |
| `hooks-present` | Medium | a hook / lifecycle declaration (implicit execution) |
| `hook-network-io` | High | a hook file that **also** makes network calls (silent auto-run + egress) |
| `deny-rules-present` | Info (positive) | explicit `deny` rules — a defensive signal |
| unpinned deps | Medium | dependency specs without a pinned version (via `auto-update-latest`) |

### A.3 The declared-vs-inferred cross-check (Stage 0 × Stage 1)

The scanner records what the author **declares** (Stage 0) and what it **infers**
from the code (Stage 1), then emits a **Discrepancies** list:

| Declared says | Scan infers | Discrepancy band |
|---|---|---|
| `makes_network_calls: false` | network IO present | High |
| `has_hooks: false` | a hook declaration present | High |
| `telemetry: false` | a telemetry endpoint present | Medium |
| `network_endpoints: [...]` | a host outside the declared set | Low |

A false declaration caught here is a strong, *verifiable, non-subjective* trust
signal. The cross-check is deliberately conservative about its own false
positives — e.g. an `AF_UNIX` socket (local IPC) is **not** counted as network,
and XML-namespace schema URLs (`schemas.openxmlformats.org`) are **not** counted
as fetched endpoints.

---

## Part B — Subjective dimensions (Stage 2, bounded AI judgment)

These need judgment a regex cannot provide. They are scored by the open
**`evaluate-repository`** engine — a static, read-only AI evaluator that is
explicit that it *"supports curation and triage, not automated approval"* and
*"prefer[s] explicit uncertainty over confident speculation."* Every item is
marked **confirmed / likely / unclear**, and the output is **labeled AI static
analysis, never human-reviewed.**

| Dimension | What it assesses |
|---|---|
| **Code quality** | structure, readability, internal consistency, presence of tests/evals |
| **Scope / academic fit** | does it do genuine scholarly-lifecycle work (lit search, OCR, stats, citation, figures, writing, peer-review) — not generic dev tooling? |
| **Claim plausibility** | do the README/SKILL.md claims match what the code actually does? |
| **Documentation honesty** | does the documentation disclose side effects, network use, and hooks — and match the implementation? |

The engine also runs a **Claude-Code-specific checklist** (does it define hooks?
do hooks run shell? does it write persistent state? implicit execution? safe
defaults? a disable mechanism?) and a **Fast-Reject heuristic** (clear malicious
behaviour / undisclosed high-risk implicit execution / severe claim-behaviour
mismatch / unsafe defaults with no mitigation).

**Division of labor, stated honestly:** Part A is reproducible code; Part B is a
bounded AI judgment; the **inclusion decision is a human curator's**, who reads
the whole dossier. The AI triages and surfaces evidence; it does not rubber-stamp
inclusion, and it never fabricates the recommendation.

---

## How the criteria combine

1. Run Part A. The deterministic scan surfaces the entry's **disclosed
   capabilities** (network, hooks, permission scope) and any place the author's
   declaration disagrees with the code; severity bands rank the findings for triage.
2. Part B contextualises the findings (real risk vs false positive) and the entry's
   scholarly value. For owner-authored entries, Part B is **recused** to an
   independent reviewer.
3. The **inclusion decision is a human curator's**, made openly on scholarly
   usefulness. There is no automated pass/fail label and no severity verdict — the
   list publishes capability facts, not a safety rating.

See [SEVERITY.md](SEVERITY.md) for the bands and [VALIDATION.md](VALIDATION.md)
for how the criteria themselves were audited and how to contest them.
