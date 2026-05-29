# Security Policy

This list indexes tooling that **runs code** — Claude Skills execute Python and
bash, declare `allowed-tools`, define hooks that fire on lifecycle events, and
can reach the network. Security is therefore not a footnote here; it is the
reason the list exists. This document explains what the capability tags do and
do **not** mean, how the disclosure check works, and how to report a problem.

## What the capability tags mean — and what they do not

> **Being on this list is not a security guarantee. You run third-party code at
> your own risk.**

Each entry surfaces objective **capability tags** drawn from its own `security:`
disclosure — `net`, `hooks`, `bypass`, plus `⚠ disclosure` when the declaration
disagrees with the code. These come from an open, deterministic static framework —
the Academic Skill **Disclosure** Framework (**ASDF**), which lives in
[`framework/`](framework/) and which anyone can read and re-run. ASDF is a
**disclosure tool, not a security audit and not a safety rating.** It reports what
a read-only script can infer about a repo and cross-checks that against the
author's declaration. It **cannot** catch everything — a determined attacker can
hide behavior behind encoding, indirection, or logic that only triggers at
runtime, and any skill can change after we look at it. Static analysis has limits,
and we would rather be honest about them than imply a safety we cannot deliver.

**No human has line-by-line audited every listed repository.** The cross-check is
code, run by an AI pipeline; it is **AI-checked, not human-reviewed** — saying
otherwise would be the exact dishonesty this framework was built to remove.

Treat every skill on the list the way you would treat any third-party code you are
about to run: read what it does, understand the permissions it asks for, and run
it in an environment you are comfortable with. **For institutional or
sensitive-data use, review the source yourself before running it** — a list entry
is a starting point for your own diligence, not a substitute for it. The tags
below exist precisely so the list never implies that everything on it is uniformly
safe.

### What the tags mean

The tags are facts about behavior, generated from machine-readable data
([`framework/analysis.yml`](framework/analysis.yml)) and the author's `security:`
block, and verified against the code by the scanner:

| Tag | Meaning |
|---|---|
| `net` | Makes network calls beyond the Anthropic API. |
| `hooks` | Defines lifecycle hooks that run automatically. |
| `bypass` | Needs `--dangerously-skip-permissions` (rare; worth knowing). |
| `⚠ disclosure` | The author's declaration disagrees with what the code shows — read it yourself. |

> **A tag is a fact, not a verdict.** A skill tagged `net` is **not** "dangerous,"
> and a skill with **no** tags is **not** "verified safe" — an untagged entry just
> declares a plain, local, no-hooks skill. The tags are disclosure, surfaced so
> you can decide for yourself; they are not a severity rating, a score, or a
> pass/fail gate. There is **no "analyzed" / "listed" verdict** — an earlier
> version assigned each entry a severity-based label and we **removed it**, because
> static severity-guessing produced too many false positives to be trustworthy
> (version strings read as IP addresses, a security tool's own block-list read as
> an attack). A label that is mostly false positives is worse than no label.

There is **no "human-reviewed" badge**, and no badge is ever shown for a review we
did not actually perform. The tags claim exactly what ASDF can state honestly —
nothing more. See [`framework/README.md`](framework/README.md) for the full
methodology and its honest limits.

## How the disclosure check works (the ASDF pipeline)

Every entry passes through the open pipeline described in
[`framework/README.md`](framework/README.md). **The script reports facts; a human
curator decides inclusion — neither step is hidden, and neither is a security
audit.**

- **Stage 0 — author declaration.** The entry's `security:` block declares the
  executable surface: network endpoints, hooks, bypass-permission needs,
  telemetry, auto-update, `allowed-tools` scope, and any commercial dependency.
  *This is the author's claim, to be checked — not proof of safety.*
- **Stage 1 — deterministic static scan**
  ([`framework/scanner/security_scan.py`](framework/scanner/security_scan.py)). A
  read-only, reproducible pattern + structure scan covering (among other things)
  pipe-to-shell and reverse-shell patterns, decode-then-execute and long
  obfuscated blobs, credential and data-exfiltration paths (`.ssh`/`.aws`/`.env`
  reads, file-read-then-POST, Discord/Slack/Telegram/Pastebin webhooks),
  miner/RAT signatures, dynamic `eval`/`exec`/`os.popen`/`child_process` sinks,
  unscoped `Bash(*)` allowlists, unpinned `@latest` / pipe-to-shell installs, and
  an enumeration of every genuine lifecycle hook. From these it infers the
  capability tags and **cross-checks the declaration against what it found**,
  raising `⚠ disclosure` on any mismatch. Same repo + same rule version → same
  findings, every run; each result records the exact scanned commit. It produces
  disclosure evidence, **never** a pass/fail gate, and never auto-approves or
  auto-rejects.
- **Stage 2 — bounded AI judgment** (the open `evaluate-repository` engine) for
  the *subjective* dimensions only — code quality, scope/academic fit, claim
  plausibility, documentation honesty — each marked confirmed / likely / unclear.
  **Labeled AI static analysis, never human review.** Applied to a
  decision-relevant subset; entries without it say so honestly.
- **Curator decision.** A maintainer reads the Stage 0–2 dossier and decides
  inclusion. The tooling discloses; a person decides. Inclusion is an editorial
  judgment about scholarly usefulness and quality, made separately and openly —
  **not** a security clearance, and never a rubber-stamp on green CI.

This is best-effort and static by design. **Honest disclosure plus a deterministic
cross-check — not a claim of human security review — are what the framework
offers.** The framework is itself audited before it is trusted and is open to
challenge: see [`framework/VALIDATION.md`](framework/VALIDATION.md).

## Reporting a vulnerability

There are two different things you might be reporting. Please use the right
channel for each.

### (a) A vulnerability in *this repository's own tooling*

If you find a security issue in **our** code — the generator scripts, the ASDF
framework, the CI workflows, the schema, anything we ship in this repo — please
report it **privately**, not in a public issue:

- Open a [**private security advisory**](../../security/advisories/new) on this
  repository (GitHub → Security → Advisories → "Report a vulnerability"), **or**
- Contact a maintainer directly via the contact methods on their GitHub profile
  (see [`CODEOWNERS`](.github/CODEOWNERS)).

Please include what you found, how to reproduce it, and the potential impact. We
will acknowledge your report, investigate promptly, and credit you when a fix
ships (unless you prefer to remain anonymous). Because this repo is "a data file
with some plumbing," its main sensitive surface is maintainer credentials and the
CI pipeline — reports about those are especially welcome.

### (b) A *listed skill* that has turned malicious or unsafe

If a skill **on the list** has started doing something harmful — exfiltrating
data, running undisclosed code, shipping a malicious update — please tell us so
we can protect users:

1. **First, report it to the skill's own maintainers** (its repository's security
   contact or issue tracker), since they can fix it at the source.
2. **Also report it to us**, privately, through either channel in (a) above, so we
   can act on our end.

We will **triage** the report and, if the problem is real and the upstream
maintainers do not address it — or the issue is serious enough to warrant
immediate action — we will **delist the skill** (a one-file removal, after which
the README regenerates without it). Persistent, serious security issues are
grounds for removal, as stated in [`CONTRIBUTING.md`](CONTRIBUTING.md#maintenance-and-removal).
A delisted skill is welcome back once the issue is resolved. Because every ASDF
result is dated and framework-versioned, staleness is visible — and a skill whose
disclosure checked out when scanned can still be reported if it later changes.

## Scope

In scope: this repository's scripts, the ASDF framework, workflows, schema, and
generated output; and reports of listed skills behaving maliciously.

Out of scope: general bugs in third-party skills that are not security issues
(open those upstream), and feature requests for this list (use a
[Discussion](../../discussions) or the enhancement issue template).

Thank you for helping keep research tooling open, inspectable, and honestly
disclosed.
