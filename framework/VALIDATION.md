# ASDF validation record

> A framework that asks others to trust its analysis must itself be audited
> *before* it is applied — and must be **contestable** afterward. This file
> records that audit and states how to challenge any check or any entry's result.
> It is the meta-level of the framework's own principle: don't ask anyone to
> trust an unvalidated instrument.

> **Historical note (disclosure refounding, 2026-06).** This records the v1 expert
> + cross-model audit of the framework when it still published an `analyzed` /
> `listed` severity verdict over an earlier, broader entry set. The framework has
> since been **refounded to disclosure-only** (capability facts, no verdict — see
> [README.md](README.md)); the verdict-specific findings below are historical. The
> audit's core conclusions — read-only, deterministic, reproducible, honestly
> labeled, and contestable — still hold for the current scanner.

## Why this file exists

The tools the security community trusts are peer-validated before they carry
authority: OpenSSF Scorecard's checks evolve via documented PRs; CVSS is a
multi-org standard owned by FIRST; CodeQL queries are reviewed in the open. ASDF
follows the same pattern — its criteria, scanner, severity bands, and
honesty-of-labeling are audited by independent reviewers, the findings are fixed
and recorded here, and the framework stays open to challenge.

## Audit scope (what reviewers check)

A validation pass audits the framework instrument itself, **not** the listed
skills, against four questions:

1. **Criteria** — are the checks in [CRITERIA.md](CRITERIA.md) the right ones, are any missing, and are the false-positive notes accurate?
2. **Scanner** — does [`scanner/security_scan.py`](scanner/security_scan.py) implement the criteria correctly, read-only, deterministically, with defensible false-positive handling?
3. **Severity** — is the [SEVERITY.md](SEVERITY.md) band assignment calibrated correctly to CVSS / OpenSSF, with each band defined by finding-type?
4. **Honesty of labeling** — do the labels and per-entry reports claim *exactly* what was done (AI-analyzed, bounded, dated) and nothing more — no "human-reviewed," no blanket "safe," explicit "listed ≠ safe"?

## Validation log

| Round | Date | Reviewer | Scope | Outcome |
|---|---|---|---|---|
| Build self-review | 2026-05-29 | Framework author (Claude) | scanner false-positive calibration on the 89-entry run | Fixed: version-string IPs, doc-file context downgrade, `AF_UNIX` local-socket vs network, XML-namespace endpoints, `__import__`/`pickle.loads` → Medium, `destructive-command` root/home-only targeting, `t.co/` vs `posit.co` shortener collision. Recorded in `CHANGELOG.md`. |
| **R4 expert audit** | **2026-05-29** | **Evaluation/security expert agent (Claude) + an independent model — OpenAI Codex (GPT-5-class) — per the project's second-opinion rule** | **criteria · scanner · severity · honesty · neutrality, against the trust-factor checklist** | **PASS with fixes (re-reviewed).** Instrument judged sound: read-only, deterministic (byte-identical reruns), reproducible, **0 leaks across all 89 entries** (no `analyzed` entry hid a High/Critical; no context-downgrade concealed a real risk). Findings raised and **all fixed in fix-round FX1** (below): scanner false-negatives, false-positive precision (doc/example two-band downgrade, `def eval`/comments, hook detection, hidden-Unicode), a missing declared-vs-inferred cross-check, reproducibility (scanned commit SHA), and three honesty failures (SEVERITY over-claim, `SECURITY.md`/`CONTRIBUTING.md` "human-reviewed" language). Owner skills recused. See the full record below. |

### R4 expert audit — full record (2026-05-29)

**Method.** An evaluation/security-expert reviewer read every framework file,
loaded the owner's `evaluate-repository` skill as the reference rubric, **re-ran
the scanner** on the owner skills, the Critical entries, and the giant suites,
verified determinism (two byte-identical reruns on the 1664-file `deepanalyze`),
re-derived the labels from the deterministic results, adversarially traced every
Critical→High context downgrade, and spot-checked per-entry reports against the
actual cloned repos. **Independently and in parallel, a different model — OpenAI
Codex (GPT-5-class), per the project's `codex-as-second-opinion` rule — audited
the same instrument** (cross-model, so a blind spot in the authoring model is not
also the blind spot of its reviewer).

**Verdict.** The ASDF *instrument* is sound, honest, and trustworthy enough to
apply: the scanner is genuinely read-only (only writes are to `stderr`; only
subprocess is a read-only shallow clone), deterministic, and reproducible; the
severity bands are correctly anchored to CVSS/OpenSSF; **0 leaks** were found
across all 89 entries (no `analyzed`/clean entry concealed a genuine
High/Critical, and no downgrade hid a real risk). The "no malware" headline was
independently re-verified on all 4 Critical entries (`claude-prism`,
`mcp-for-stata`, `gpt-researcher`, `deepanalyze` — all benign official-installer
or `chmod 777` patterns, correctly held at `listed`, not sanitized away).

**Findings (all addressed in fix-round FX1 below).**

*Scanner false-negatives (Codex).* The pattern set missed several reverse-shell /
exfil / exec forms: `nc host port -e /bin/sh` (flags after host), `socat …
EXEC:/bin/sh`, a Python `socket.connect` + `subprocess`/`Popen` pair split across
lines, `os.popen(...)`, `child_process.exec(...)`, bare `Popen(…, shell=True)`,
multiline decode-then-exec, and `requests.post("http…", data=open(...))`-style
file-read-then-POST exfiltration.

*Scanner safety / reproducibility (Codex).* No symlink guard (a committed symlink
could cause a read outside the clone — e.g. `creds → ~/.aws/credentials`); reports
did not record the **scanned commit SHA**, so "same repo → same findings" was not
pinned to a commit.

*Scanner precision (R4 F-1…F-4 + Codex).* A dangerous string in documentation /
example-data was downgraded only one band, leaving credential/destructive
patterns at High (confirmed live FP: a `/etc/passwd` line inside *Think Python*
textbook prose in `marker`); `dangerous-eval-exec` fired on `def eval`/`class
Eval`/commented code; **hook detection flagged React/frontend `src/hooks/` paths
and even prose mentions of the word "hooks"** as agent lifecycle hooks (confirmed
live FP: `education-agent-skills`, flagged because a SKILL.md said "genuine hooks
— students notice them"); `hidden-unicode` flagged a deliberate, named ZWSP
feature in `ssci-plots`'s `scripts/ssci_style.py` as if it were Trojan-Source.

*A missing cross-check (R4 F-3).* The cleanest declared-vs-inferred catch — an
`allowed_tools_scoped: true` declaration contradicted by an inferred unscoped
`Bash` — was not wired into the deterministic cross-check.

*Honesty failures (R4 B-2, Codex #7).* `SEVERITY.md` over-claimed CVSS
"calibration" (it borrows band *names*; it does not compute vectors).
`SECURITY.md` and `CONTRIBUTING.md` still documented a `✅ security-reviewed`
"independent human review" badge and called "human Tier-2 review … the real
defense" — directly contradicting `framework/README.md`'s "AI-analyzed, not
human-reviewed." (The legacy per-entry `trust_tier: reviewed` / `security_review`
data fields and the schema/recusal-lint keyed to them were removed by the lead in
the same redesign pass; trust now lives only in `analysis.yml` + the per-entry
reports.)

**Independent Codex cross-model review — owner-skill recusal verdict.** The
independent reviewer examined the two owner-authored entries (recusal-relevant):
it **confirmed `paper-search-pro` as `listed`** (a bare, unscoped `Bash` in
`allowed-tools` — a genuine over-permission), and **could not access the
`ssci-plots` source**, so it produced **no independent subjective sign-off** for
it. Because `analyzed` carries a subjective sign-off the maintainer must not give
for their own work, **both owner skills are held at `listed`** pending an
independent reviewer: `paper-search-pro` on a real finding, `ssci-plots` because
no independent subjective sign-off exists yet (its deterministic scan is clean).
The recusal is recorded in each entry's report and is now enforced
deterministically in the pipeline (an owner-authored entry is never auto-badged
`analyzed`).

**Fixes applied (fix-round FX1, 2026-05-29).** All of the above were fixed and the
scanner was re-run over all 89 entries, regenerating `reports/*.md` +
`analysis.yml`:

1. **Scanner hardened** (`scanner/security_scan.py` + `scanner/rules/`): added the
   missing reverse-shell/exfil/exec patterns (new `reverse-shell-py`,
   `shell-exec-spawn`, `exfil-data-read` rules + a broadened `reverse-shell` and
   multiline `decode-then-exec`); added a **symlink guard** (never follows a
   symlink, never reads outside the clone); a **two-band** downgrade for
   credential/destructive/exfil/shell patterns in documentation *and*
   example-data files; excluded `def eval`/`class Eval`/commented code from
   `dangerous-eval-exec`; **re-scoped hook detection to genuine Claude/agent
   lifecycle hooks only** (a `hooks:` config key or a `.claude/hooks/`-style dir),
   explicitly excluding frontend `src/hooks/` paths; down-weighted
   `hidden-unicode` in a named string literal; wired the **`allowed_tools_scoped`**
   declared-vs-inferred discrepancy; and **recorded the scanned commit SHA** in
   every report. Kept read-only + deterministic (re-verified byte-identical).
2. **Report misstatements fixed.** `anthropic-pdf` (and every entry without an
   individual Stage-2) no longer claims "bounded AI judgment" in its header — it
   states the subjective stage was not individually applied. `ssci-plots`'
   hidden-Unicode finding is described correctly as a *documented optional ZWSP
   feature in `scripts/ssci_style.py`* (down-weighted to Low), not a
   "documentation pattern."
3. **`SEVERITY.md`** reworded: the band **names are anchored to** CVSS/OpenSSF
   conventions; no CVSS vector is computed (the ranges are orientation, not a
   score).
4. **`SECURITY.md` + `CONTRIBUTING.md` rewritten** to the honest framing: every
   entry is AI-analyzed via the open ASDF framework — a best-effort static
   pre-screen, **not a security audit**; **`listed` ≠ safe and `analyzed` ≠ safe**;
   a curator decides inclusion (AI triages, a human decides); review the source
   before institutional use; the report-and-delist process for a listed skill that
   turns malicious is preserved. All "✅ security-reviewed / independent human
   review / human review is the real defense" language removed; consistent with
   `framework/README.md`.

**Re-review.** After FX1, the only label movements vs the prior run were the two
intended ones: `ssci-plots` `analyzed → listed` (owner recusal) and
`education-agent-skills` `listed → analyzed` (the false "hooks" prose match was
removed — a correct false-positive fix, verified to hide no real finding). The 4
Critical entries remained Critical/`listed`. Distribution: **45 `analyzed` · 44
`listed`** of 89.

### Known limitations carried into R4 (author-declared)

Honest entries for reviewers to weigh — these are not hidden:

- **Static only.** No dynamic / taint analysis; runtime-only and heavily-obfuscated behaviour is out of reach. A clean scan is not proof of safety.
- **Stage 2 coverage is partial in v1.0.** The subjective dimensions were AI-scored for a decision-relevant subset (owner skills, representative clean entries, the most context-needing findings); other entries carry the deterministic Stage 0/1 plus an honest "Stage 2 available on demand" note. Reviewers should decide whether broader Stage-2 coverage is required before launch.
- **`rules_version` fingerprints `patterns.yml` only.** The structural checks and inference logic live in the scanner `.py`; a future version may fingerprint the whole instrument. (As of FX1 each report also records the **scanned commit SHA**, so the *repository* side of "same repo + same rules → same findings" is now pinned to an exact commit; the remaining gap is fingerprinting the `.py` logic itself.)
- **Large-suite handling is a file-count heuristic** (a `suite`/`tool` above a threshold is `listed` as unauditable). Reviewers should sanity-check the threshold.
- **Declared-vs-inferred network inference** is conservative but imperfect (it excludes `AF_UNIX` and XML namespaces); a determined under-discloser using an unusual transport could still slip a discrepancy.

## Contest channel — challenge any check or any verdict

Like pip-audit (`--ignore-vuln` + an open false-positive FAQ) and semgrep
(rules are PR-able by anyone), ASDF is contestable:

- **A rule / criterion is wrong, too broad, or missing** → open an issue or PR
  against [`scanner/rules/`](scanner/rules/) and/or [CRITERIA.md](CRITERIA.md).
  The rules are readable data; propose the exact change.
- **An entry's result is a false positive (or a missed true positive)** → open an
  issue referencing the per-entry report in [`reports/`](reports/); include the
  file/line and why the finding is benign (or why a clean entry should be
  flagged). Re-running the scanner is the first step (`python
  framework/scanner/security_scan.py --repo <url>`).
- **A label over- or under-claims** → the labels are deliberately bounded
  (`analyzed` = clean static pre-screen, not a safety guarantee; `listed` ≠
  unsafe). If a report's wording implies more than was done, that is a bug —
  report it.
- **A listed skill turns malicious** → see the repo-level `SECURITY.md` for the
  report-and-delist process; ASDF results are dated so staleness is visible.

All challenges are resolved in the open. A verdict here can be wrong; saying so
is part of why it can be trusted.

---
<sub>ASDF v1.0 · validation record · 2026-05-29 (R4 expert audit + independent
Codex cross-model review + FX1 fixes recorded). The instrument is itself auditable
and contestable.</sub>
