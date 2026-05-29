# Contributing to Awesome Academic Skills

Thank you for helping build this list. The goal is simple: a vendor-neutral,
carefully curated index of the **best Claude Skills and adjacent agent tooling
for academic and research work** — across the whole scholarly lifecycle, for
every discipline, in English and 中文.

We would genuinely love your help finding skills we have missed. Nominating
someone else's great work is just as welcome as submitting your own. This guide
explains what belongs here, how to contribute, and the one thing that makes this
list trustworthy: **every entry surfaces its own disclosed capabilities (network,
hooks, permission scope), cross-checked against the code by an open, deterministic
framework; a human curator decides what to include; and we are honest about
exactly what that does and does not promise — the tags are facts, not a safety
rating.**

If anything below is unclear, please open a [Discussion](../../discussions) and
ask — improving this guide is itself a valuable contribution.

## Contents

- [What belongs here](#what-belongs-here)
- [Two ways to contribute](#two-ways-to-contribute)
- [Eligibility](#eligibility)
- [The data contract](#the-data-contract)
- [Security disclosure (required)](#security-disclosure-required)
- [Validate your claims](#validate-your-claims)
- [How the disclosure check works](#how-the-disclosure-check-works)
- [Submitting your own skill (and our neutrality promise)](#submitting-your-own-skill-and-our-neutrality-promise)
- [Maintenance and removal](#maintenance-and-removal)
- [The badge](#the-badge)

## What belongs here

This list indexes tooling that helps researchers do real scholarly work with
Claude and agentic AI, organized by where it fits in the research lifecycle:
literature discovery, reference management, reading and summarization, PDF/OCR,
data analysis and statistics, figures, academic writing, writing quality and
de-AI, grants, peer review, submission and formatting, plus the bigger building
blocks — skill suites, autonomous research systems, MCP servers, discipline
packs, and ecosystem maps.

Concretely, an entry can be a:

- **Skill** — a single Claude Skill (a `SKILL.md` plus its assets)
- **Suite** — a multi-skill repository or collection
- **MCP server** — a Model Context Protocol server useful in research workflows
- **Tool** — a CLI or library that pairs naturally with an agent workflow
- **Plugin** — a Claude Code plugin
- **List** — an awesome list or ecosystem map worth pointing to

**This is a curated list, not an exhaustive catalogue.** The README shows the
best of each category — the entries we would actually recommend to a colleague.
Breadth lives in the data layer (`data/skills/`); the rendered list is the
distilled best. If your favorite skill is excellent but niche, it can still earn
a place — quality and a genuine, specific reason to recommend it matter more than
popularity.

What does **not** belong: closed-source products with no inspectable repository,
abandoned or non-working tooling, anything whose primary purpose is to funnel
users to a paid product, and anything unrelated to academic or research work.

## Two ways to contribute

Both paths feed the **same** [data contract](#the-data-contract), so pick
whichever is comfortable — there is one review process behind both.

### Track A — Issue Form (recommended for everyone)

Open a [**Recommend a skill**](../../issues/new?template=recommend-skill.yml)
issue and fill in the form. It collects everything we need, validates your input,
and a maintainer takes it from there — on approval, a bot turns your form into a
`data/skills/<slug>.yml` entry and opens the pull request for you. You never have
to touch YAML.

This is the lowest-friction path and the one most contributors should use.

### Track B — Data PR (for power users)

Comfortable with YAML and Git? Add a single
`data/skills/<your-skill>.yml` file on a branch and open a pull request. CI runs
the full set of checks, a maintainer reviews, and on merge the README is
regenerated automatically. See the [data contract](#the-data-contract) and the
pull-request template for the exact shape. One skill per pull request, please.

> **Submissions must be made by a human.** AI may have *written* the skill you
> are recommending — that is completely fine, and many excellent skills are
> AI-assisted. But the *recommendation itself* must come from a person who has
> looked at the skill and thinks it is worth listing. Please do not have an agent
> auto-file submissions on your behalf; you are responsible for anything submitted
> under your account. This is what keeps the list a human-curated resource rather
> than a scraped pile, and it is a hard requirement.

## Eligibility

We keep the bar light but real, so the list stays trustworthy without being
gatekept:

- **The repository is public and at least 7 days old** (measured from its first
  public commit). Skills move fast, so we do not require a months-old release —
  but a brand-new, empty repo is not ready to recommend yet.
- **The license is present and identifiable.** A clear open-source license
  (MIT, Apache-2.0, BSD, GPL, etc.) is ideal. A non-commercial license
  (`CC-BY-NC`) or no license at all is **allowed but flagged** — it is not a
  blocker, but users deserve to know, so it must be stated, never left blank.
- **There is a real README** explaining what the skill does, and — for a skill or
  suite — enough that we can actually try it (see [Validate your
  claims](#validate-your-claims)).
- **It is not abandoned or non-working**, and it is not a name-squat or a thin
  wrapper that exists only to advertise a paid product.

If a repo only just misses the age bar, no problem — submit it again in a few
days. We are not trying to turn anyone away.

## The data contract

Every entry is one YAML file at `data/skills/<slug>.yml`, validated in CI against
[`schema/skill.schema.json`](schema/skill.schema.json). The README you see is
**generated** from these files — you never edit the README directly. The schema
is the single source of truth for field names, types, and which fields are
required; the summary below is a friendly orientation, not a substitute for it.

**Required (you supply these):**

| Field | What it is |
|---|---|
| `name` | Display name, e.g. `paper-search-pro` |
| `slug` | kebab-case identifier, matching the filename |
| `source_url` | Canonical GitHub repository URL (the real one, after any rename/redirect) |
| `author` | Real author/org name or handle |
| `author_url` | `https://github.com/<author>` |
| `license` | SPDX identifier (e.g. `MIT`); `No License` is permitted but flagged |
| `category` | One category from the lifecycle taxonomy (see the issue form's dropdown) |
| `lifecycle_stage` | Where it fits: `discovery`, `citation`, `reading`, `ocr`, `analysis`, `figures`, `writing`, `writing-quality`, `grant`, `peer-review`, `publishing`, `suite`, `autonomous`, `mcp`, `discipline`, or `meta` |
| `type` | `skill`, `suite`, `mcp-server`, `tool`, `plugin`, or `list` |
| `description` | ≤250 characters; see the style rules below |
| `security` | The disclosure block — see [Security disclosure](#security-disclosure-required) |

**Recommended (optional, but they help):** `homepage_url`, `install` (a one-line
install hint), `validate_claim` (**required for a skill or suite** — see below),
`lang` (e.g. `[en]` or `[en, zh]`), `tags`.

**Machine-maintained:** the per-entry disclosure cross-check lives in
[`framework/analysis.yml`](framework/analysis.yml) (a `disclosure_mismatch` flag
written by ASDF, not stored per-entry), and the live-metadata fields
(`stargazers_count`, `updated_at`, `archived`, `current_release`,
`last_link_check`, `last_security_scan`) are filled in by CI. Leave them out — they
are not yours to set. There is **no `trust_tier` / `security_review` field**: there
is no trust score to set. The only machine-derived signals are the objective
capability tags, surfaced by the open, re-runnable ASDF cross-check — never a
hand-set "reviewed" tier.

### Description style

The description is the heart of the list, so we hold it to a specific style:

- **≤250 characters**, sentence case, ending with a period.
- **Descriptive, not promotional.** Say what it *does* and what it is good (and
  not good) at. "The one to start a literature review with; weak at non-English
  sources" is great. "The ultimate revolutionary AI research assistant!!" is not.
- **Do not address the reader** ("you can…") and **do not restate the repo's own
  tagline** — write a fresh, specific, honest line, ideally from having actually
  used the skill.
- **No emoji.**

A good description is the difference between a list a person made and a list a
scraper made. It is worth the extra minute.

## Security disclosure (required)

Skills run code — Python, bash, lifecycle hooks — and can reach the network. That
is exactly why this list exists: to be a place where someone has actually looked.
So every submission must **disclose its executable surface**. You are not being
accused of anything; you are giving reviewers and users the facts they need.

For every entry, declare:

- **Network calls** — does it make any network request beyond the Anthropic API?
  If yes, **list every endpoint** it talks to.
- **Hooks** — does it define any lifecycle/stop hooks that run automatically? If
  yes, describe each hook and what triggers it.
- **Bypass permissions** — does it need `--dangerously-skip-permissions` (or any
  permission-bypass mode)? If yes, say why, and make sure users are warned.
- **Telemetry** — does it phone home with usage data?
- **Auto-update** — does it self-update or pull `@latest` at runtime (e.g.
  `npx …@latest`)? This is a known supply-chain vector and will be looked at with
  care.
- **`allowed-tools` scope** — is the tool allowlist specific, or does it use a
  `Bash(*)` wildcard? A scoped allowlist is a positive signal; a wildcard must be
  justified.
- **Third-party dependency** — does it require a commercial/paid product or a
  proprietary API to function at all?

Two further rules:

- **Any bash script a user is expected to run must be commented** so its behavior
  is auditable.
- **Run the ASDF static scan on the repo before submitting** if you can:
  `python framework/scanner/security_scan.py --repo <your-repo-url>`. It is the
  same read-only, deterministic scan that runs during the disclosure check, so
  running it yourself first surfaces the capability tags and catches any
  declaration-vs-code mismatch early. The rules are open data in
  [`framework/scanner/rules/`](framework/scanner/rules/) — read exactly what it
  checks.

A disclosure that turns out to be false (you said "no network calls" but the code
ships a webhook) is a strong signal *against* listing — not because the behavior
is necessarily malicious, but because the list runs on honest disclosure.

## Validate your claims

For a **skill or suite, this is mandatory**: give us a concrete, low-friction way
to see the skill actually work. The best form is a specific task plus the exact
prompt you would hand Claude, and what a correct result looks like. For example:

> *Ask Claude to find five recent papers on CRISPR off-target effects across all
> five sources, then verify every returned DOI resolves.*

This lets a reviewer confirm the skill does what it claims in a couple of minutes,
and it is one of the strongest things you can include to get an entry approved
quickly. For tools, MCP servers, and lists, it is encouraged but not required.

## How the disclosure check works

Every submission goes through the **Academic Skill Disclosure Framework
([`framework/`](framework/))** — an open, deterministic, re-runnable static check.
The principle behind it: **the script reports facts; a human curator decides; we
never claim a human security audit we did not perform, and we never auto-approve
on green CI.** ASDF is documented in full in
[`framework/README.md`](framework/README.md); the short version:

1. **Stage 0 — your disclosure.** The security block above is your *declared*
   capability — a claim, to be checked.
2. **Stage 1 — deterministic static scan.** A read-only pattern + structure scan
   over the submitted repo
   ([`framework/scanner/`](framework/scanner/)): obfuscated/decode-then-run code,
   credential and exfil patterns (incl. file-read-then-POST), reverse shells,
   `eval`/`exec`/`os.popen`/`child_process` sinks, unscoped `allowed-tools`,
   unpinned `@latest`/pipe-to-shell, and an enumeration of genuine lifecycle
   hooks. From these it infers the capability tags and **cross-checks your
   disclosure against what it found**, records the scanned commit, and is
   reproducible (same repo + same rules → same findings). It produces disclosure
   evidence, **never** a pass/fail gate, and never auto-approves or auto-rejects.
3. **Stage 2 — bounded AI judgment.** The open `evaluate-repository` engine scores
   the *subjective* dimensions (quality, scope/fit, claim plausibility,
   documentation honesty), each marked confirmed / likely / unclear. **Labeled AI
   static analysis, never human review.**
4. **Curator decision.** A maintainer reads the dossier and decides inclusion —
   an editorial judgment about scholarly usefulness and quality, **not** a security
   clearance.

The outcome is not a score or a verdict — it is the entry's **capability tags**,
surfaced next to it and recorded as a `disclosure_mismatch` flag in
[`framework/analysis.yml`](framework/analysis.yml):

- **`net`** — makes network calls beyond the Anthropic API.
- **`hooks`** — defines lifecycle hooks that run automatically.
- **`bypass`** — needs `--dangerously-skip-permissions`.
- **`⚠ disclosure`** — your declaration disagrees with what the code shows.

An entry with none of these declares a plain, local, no-hooks skill. **The tags
are facts, not a safety rating: a `net` tag is not "dangerous," and an untagged
entry is not "verified safe."** There is **no `analyzed` / `listed` severity
verdict** (we removed it — static severity-guessing produced too many false
positives to trust) and **no "security-reviewed" / "human-reviewed" badge** —
that would claim a line-by-line human audit that does not happen. See
[`SECURITY.md`](SECURITY.md) for what the tags do and — importantly — do **not**
mean, and remember you run third-party code at your own risk. If you fix something
the cross-check flagged, ask for a re-scan.

## Submitting your own skill (and our neutrality promise)

**Yes, please submit your own skill** — most submissions to lists like this are
self-authored, and that is expected and welcome. It competes on equal footing:
same data contract, same disclosure, same deterministic scan. There is no
preferential placement; ordering within a category is generated deterministically
from the data, not hand-arranged to float anyone's work.

You should also know this, because neutrality only counts if it is stated plainly:

> **This list is maintained by an author of some of the skills it lists.** Those
> skills go through the *identical* ASDF disclosure check as every other entry —
> same capability tags, same declaration-vs-code cross-check — and the maintainer
> **recuses** from the subjective sign-off on their own work: the inclusion call on
> an owner-authored entry is **never made on the maintainer's say-so alone**, but
> deferred to an **independent** reviewer (a different model, e.g. an independent
> Codex cross-model review, or a co-maintainer) for the subjective dimensions. The
> deterministic Stage-1 scan is the same for everyone and anyone can re-run it.
> Owner entries receive **no preferential placement and no special treatment**,
> and their authorship is shown openly, not hidden. If you know a better skill in
> any category — including one that beats the maintainer's own — **submit it.** It
> will be judged on exactly the same terms, and we would rather list the best tool
> than our own.

That promise is the whole point of a *neutral* index, and we hold ourselves to it.

## Held for improvement (the backlog)

A curated list says "no" far more often than "yes" — but a useful "no" tells you *why* and
*what would change it*. So skills we discover and review but do **not** list are recorded,
constructively, in [`data/backlog.yml`](data/backlog.yml): each entry notes the specific,
usually-fixable reason it is held (thin README, missing license, no `SKILL.md`, near-duplicate
of a stronger entry, too new, or a generic wrapper with no academic-specific value) and what
would get it listed.

This is a **tracking record, not a blacklist.** The reasons are AI-assisted static assessments
from a discovery sweep, not final judgments — and skills move fast, so a "held" entry is an
invitation, not a verdict:

- **If your skill is in the backlog and you've improved it**, open a
  [**Request a re-review**](../../issues/new?template=request-rereview.yml) issue. A maintainer
  re-runs the open analysis framework and reconsiders it on exactly the same terms as every
  other entry.
- **If you think an entry is wrong** (mis-scoped, the reason is outdated, already fixed), say so
  in the same issue — we would rather correct the record than keep a stale "no".

Nothing about the backlog is permanent, and getting listed from it is the expected, welcome
path — many good skills simply need a license file and a usage example.

## Maintenance and removal

Listing is not forever — a curated list has to stay current to stay useful. We
re-check entries over time (links, activity, and a periodic re-scan), and an entry
may be **removed** when:

- its links are persistently broken,
- the project is **abandoned** (no meaningful activity for roughly 6–12 months),
- it stops working, or
- it develops **persistent, serious security issues**.

Removal is not a judgment on you — it keeps the list honest. If a delisted skill
gets revived or fixed, it is welcome back.

**Found a listed skill behaving badly?** Please report it — see
[`SECURITY.md`](SECURITY.md). We will triage it and, if warranted, delist it.

## The badge

If your skill is listed, you are welcome to add a badge to your repo's README:

```markdown
[![Listed in Awesome Academic Skills](https://img.shields.io/badge/Listed%20in-Awesome%20Academic%20Skills-000?style=flat-square)](https://github.com/O0000-code/awesome-academic-skills)
```

Thank you for contributing — and for helping keep research tooling open,
inspectable, and well-curated.
