# ASDF — the Academic Skill **Disclosure** Framework

> **An open, deterministic, reproducible way to surface what each listed skill actually
> does — network, hooks, permission scope — and to cross-check that against the author's
> own declaration. It is a disclosure tool, not a security audit and not a safety rating.**

## What this is (and what it deliberately is *not*)

Every entry in this list declares its executable surface (does it make network calls? run
lifecycle hooks? need permission bypass? what tool scope?). This framework's job is to make
that disclosure **checkable**: a read-only script reads the repo, reports the capabilities it
can infer, and flags any place the declaration disagrees with the code.

That is the whole claim. In particular it is **NOT**:

- **not a safety rating** — a skill tagged `net` is not "dangerous," and an untagged skill is
  not "verified safe." The tags are facts about behaviour, nothing more.
- **not a security audit** — no human has line-by-line audited every repo, and a static script
  can be evaded. Review third-party code yourself before running it.
- **not a pass/fail gate** — there is no score and no verdict. Inclusion in the list is a human
  curator's editorial judgement about scholarly usefulness, made separately and openly.

> ### Why no "analyzed / listed" verdict anymore
> An earlier version of this framework assigned each entry a severity-based `analyzed` /
> `listed` label. We **removed it.** Static severity-guessing on 300+ repos produced too many
> false positives to be trustworthy — version strings read as IP addresses, a security tool's
> own block-list read as an attack, a UI placeholder read as a destructive command. A label
> that is mostly false positives is worse than no label: it makes a clean skill look risky and
> trains readers to ignore the one that isn't. So the framework now reports only what a script
> can state honestly — **disclosed capabilities + a declaration-vs-code cross-check** — and
> drops the severity verdict entirely.

## The capability tags

These appear on each entry in the README and on the site. They come straight from the entry's
own `security:` disclosure block (verified against the code by the scanner):

| Tag | Meaning |
|---|---|
| `net` | Makes network calls beyond the Anthropic API |
| `hooks` | Defines lifecycle hooks that run automatically |
| `bypass` | Needs `--dangerously-skip-permissions` (rare; worth knowing) |
| `⚠ disclosure` | The author's declaration disagrees with what the code shows |

An entry with none of these declares a plain, local, no-hooks skill. **None of these tags is a
judgement** — they are disclosure, surfaced so you can decide for yourself.

## What ships here

```
framework/
  README.md            ← this file: the disclosure model, stated honestly
  scanner/
    security_scan.py   the runnable, read-only script: infers capabilities + cross-checks
                       the declaration; reports facts. (It still computes internal severity
                       bands for its own triage output, but those NO LONGER drive any
                       published label — see "Why no verdict" above.)
    rules/             the open pattern + structural rules, as readable data
  analysis.yml         per-entry disclosure cross-check result (disclosure_mismatch flag)
  CRITERIA.md          what the script checks, defined  (severity bands are advisory only now)
  SEVERITY.md          the band definitions  (retained for the scanner's own output; not a verdict)
  VALIDATION.md        how the checks were audited, and how to contest one
  CHANGELOG.md         framework versioning
```

## Run it yourself (reproducibility)

```bash
# infer a local clone's capabilities + show findings
python framework/scanner/security_scan.py path/to/repo

# shallow-clone a repo read-only and check it
python framework/scanner/security_scan.py --repo https://github.com/owner/repo

# cross-check an author declaration (declared vs inferred)
python framework/scanner/security_scan.py path/to/repo --declared decl.json
```

The scanner is read-only, runs no repository code, installs nothing, and never exits non-zero
on findings — it produces disclosure evidence, not a pass/fail gate. Its only dependency is
PyYAML.

## Neutrality

Entries are ordered alphabetically within each category by the generator — there is no lever to
float favoured entries. The list is maintained by an author of some listed skills; those skills
are held to the identical disclosure check, get no preferential placement, and their authorship
is shown openly.

---
<sub>ASDF · open · deterministic · reproducible · a disclosure tool, not a safety rating.
Capability tags are facts; review third-party code before running it.</sub>
