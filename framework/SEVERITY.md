# ASDF severity bands

The framework places every finding into one of four ordered bands —
**Critical · High · Medium · Low** — plus an **Info** tier for positive/context
signals that never count against an entry. The band *names and ordering* are
deliberately **anchored to the conventions the security community already uses**
(CVSS's named bands, OpenSSF's per-check risk levels), so "High severity" here
means roughly what it means everywhere else, rather than an invented 1–5 score
with no published anchor.

> **Honest scope of the word "calibrated."** ASDF **borrows the band names and
> their ordering** from CVSS/OpenSSF and assigns each *finding-type* to a band by
> hand. It does **not** compute a CVSS vector, does **not** derive a 0.0–10.0
> base score, and does **not** claim numerical equivalence to a CVSS rating. The
> CVSS ranges shown below are an *orientation* ("this band is in the spirit of
> CVSS High"), not a computed result. Treat the bands as a documented, ordered,
> finding-type taxonomy — not as CVSS scores.

## Why these four bands

| Source | What we borrow |
|---|---|
| **CVSS v3.1** (FIRST.org) | The four **named bands and their ordering** (None / Low / Medium / High / Critical) and the qualitative ranges those names connote (Low `0.1–3.9` / Medium `4.0–6.9` / High `7.0–8.9` / Critical `9.0–10.0`). We adopt the *names*; we do not compute the scores. |
| **OpenSSF Scorecard** | The discipline that **each finding-type carries a documented `Critical / High / Medium / Low` risk level** with a published rationale — assigned by hand to a check, not derived from a vector. |
| **semgrep** | The "severity is a property of the rule, declared in readable data" approach (`scanner/rules/patterns.yml`). |

CVSS is built to score CVEs, not skill-capability risk, so ASDF does **not**
compute a CVSS vector and does **not** produce a 0.0–10.0 score. Instead it uses a
band set whose **names are anchored to CVSS/OpenSSF** and where each band is
defined by **what kind of finding lands in it** — which is what a static
capability scan can actually determine. This is the same adaptation OpenSSF makes
when it assigns risk levels to repo-health checks by hand rather than computing
them for CVEs.

## The bands, defined by finding-type

### Critical
A strong signal of exfiltration, malware, or credential theft — the kinds of
finding that, if real, mean *do not run this*. A human **must** read these before
any trust.

- reverse shell (`/dev/tcp/`, `nc -e`, `bash -i`, `socket.connect`, `pty.spawn`)
- decode-then-execute (`base64 -d | sh`, `b64decode(...)→exec/eval`, `atob(...)→eval`)
- credential / secret-path reads (`.ssh/id_*`, `.aws/credentials`, `/etc/shadow`, `.netrc`, `.git-credentials`)
- hard-coded chat/webhook exfil endpoints (Discord/Slack/Telegram webhooks, `webhook.site`, `requestbin`)
- cryptominer / RAT / offensive-tooling signatures (`xmrig`, `stratum+tcp://`, `mimikatz`, `meterpreter`)
- dangerous PowerShell (`IEX`, `DownloadString`, `FromBase64String`, `-EncodedCommand`)
- destructive commands targeting **root / home / bare wildcard** (`rm -rf /`, `rm -rf ~`, `rm -rf $HOME`, `chmod 777`, fork bomb, raw `dd` to a disk device)

> In the spirit of CVSS Critical/High (≈ 7.0–10.0; orientation, not a computed
> score): high impact, and for the exec/exfil classes, low attacker effort once
> the skill is enabled.

### High
A real dynamic-execution or exfil-capable surface, or a **declared-vs-inferred
mismatch** — findings that genuinely need a human read but are not, by
themselves, proof of malice.

- dynamic code execution (`eval(`, `exec(`, `Function("..."`, unsafe `yaml.load`, `os.system(`, `subprocess(..., shell=True)`)
- URL shorteners / paste-raw / tunnels / Tor (`bit.ly`, `pastebin.com/raw`, `ngrok`, `trycloudflare`, `.onion`)
- hard-coded **public** IP address (real IPv4, not a version string — see false-positive handling)
- `allowed-tools` with `Bash(*)` or **unscoped `Bash`** (unrestricted shell — the widest execution surface)
- a hook/lifecycle file that **also makes network calls** (silent auto-run + egress)
- **Discrepancy:** the author declared `makes_network_calls: false` / `has_hooks: false` but the scan inferred otherwise (under-disclosure)

> In the spirit of CVSS Medium/High (≈ 4.0–8.9; orientation, not a computed
> score): a capability worth scrutiny; impact depends on how the capability is
> used, which static analysis cannot fully decide.

### Medium
Supply-chain or disclosure-worthy findings — **disclose and justify, not
disqualifying**. These are the things a careful user wants to know about before
running, but they are routine in legitimate tooling.

- pipe-to-shell install (`curl … | sh`) — *even official installers do this* (rustup, uv); flag-not-fail
- unpinned / auto-updating dependency (`@latest`, `pip install -U`, `cargo install --git`)
- dynamic import-by-name (`__import__`) or untrusted deserialization (`pickle.loads`, `marshal.loads`) — usually the standard lazy-import idiom or a tool's own cache
- hooks / lifecycle execution present (implicit execution to enumerate)
- prompt-injection / jailbreak markers (often legitimate test fixtures or guardrail examples)
- hidden / bidirectional Unicode (Trojan-Source class)
- a missing `LICENSE` file

> In the spirit of CVSS Low/Medium (≈ 0.1–6.9; orientation, not a computed score): worth disclosing; not an exploit on its own.

### Low
Weak signals and context. The scan surfaced nothing requiring escalation.

- analytics / telemetry endpoint (matters mainly as a *declared-vs-inferred* discrepancy)
- the baseline band when no finding rises above it

> In the spirit of CVSS None/Low (≈ 0.0–3.9; orientation, not a computed score).

### Info (not a band)
Positive or contextual signals that are reported but **never** count against an
entry: `license-present`, `deny-rules-present` (an explicit deny list is a
*defensive* signal).

## What the bands are for (advisory triage, not a published verdict)

The bands rank the scanner's own findings so a reader can triage them — a `High`
exfil pattern deserves a look; a `Low` missing-license note does not. They are an
**advisory signal inside the scan output, not a published label.** An earlier
version of this framework mapped the top band to an `analyzed` / `listed` verdict
on every entry; that was **removed** because static severity-guessing produced too
many false positives to trust (version strings read as IPs, a security tool's own
block-list read as an attack). The list now publishes each entry's **disclosed
capabilities** (network, hooks, permission scope) cross-checked against the code —
facts, not a safety rating. See [README.md](README.md) for the disclosure model.

A high band is honest, not a verdict of "unsafe": most are an unscoped `Bash`, an
official `uv` installer, or a security tool's own test fixtures — the scan output
says exactly what was found.

## Context downgrades (recorded, never silent)

Two adjustments keep the bands honest by cutting predictable false positives.
Both are **always recorded** in the per-entry report:

1. **Documentation files** (`.md`, `.markdown`, `.txt`, `.rst`): a dangerous
   *pattern* in a doc is almost always a command being *documented* (an install
   step, an uninstall instruction, a "this is blocked" example) rather than code
   the skill runs. Such findings are **downgraded one band**. Scripts
   (`.py`, `.sh`, `.ps1`, …) keep full severity.
2. **`bare-public-ip`** is suppressed in dependency manifests (version pins like
   `1.27.2.3` look like IPs) and in recorded HTTP test cassettes / fixture data
   (cookie tokens and page fragments produce torrents of false matches).

These downgrades, the per-rule severities, and the false-positive notes all live
in readable data (`scanner/rules/`) so anyone can audit or contest them — see
[VALIDATION.md](VALIDATION.md).
