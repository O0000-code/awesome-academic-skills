<!--
Thanks for contributing!

Most skill additions come through the Issue Form (Issues → "Recommend a skill"),
which a maintainer turns into a data entry for you — no YAML required. Direct
pull requests are great for: data edits and fixes, docs/tooling improvements, and
power users who prefer to write the YAML themselves.

If this PR ADDS or EDITS a skill, please fill in the sections below. If it is a
docs/tooling fix, delete the skill sections and just describe the change.
-->

## What does this PR do?

<!-- One sentence. For a new skill: "Adds <name> to <category>." -->

## Type of change

- [ ] New skill entry (`data/skills/<slug>.yml`)
- [ ] Edit to an existing entry
- [ ] Docs / governance change
- [ ] Tooling / generator / CI change
- [ ] Other (describe above)

---

<!-- ===== Fill in this block ONLY for a new or edited skill entry ===== -->

## New / edited skill

> One skill per pull request. Edit a single `data/skills/<slug>.yml` file
> (kebab-case slug == filename). Do not edit `README.md` / `README.zh-CN.md` —
> they are generated from the data. Remove optional fields you are not using.

### Required fields (in the YAML)

- **Name**:
- **Source URL** (canonical GitHub repo, after any rename/redirect):
- **Author**:
- **Author URL**:
- **License** (SPDX id; `No License` / non-commercial is allowed but flagged — never blank):
- **Category** (one lifecycle category — see CONTRIBUTING):
- **Lifecycle stage**:
- **Type** (`skill` | `suite` | `mcp-server` | `tool` | `plugin` | `list`):
- **Description** (≤250 chars, sentence case, descriptive not promotional, do not address the reader, no emoji):

### Security disclosure (required — see [CONTRIBUTING §Security disclosure](../blob/main/CONTRIBUTING.md#security-disclosure-required))

Check each statement that is **true**; if one is not true, leave it unchecked and
explain under "Details".

- [ ] Makes **no** network calls except to the Anthropic API — or every external endpoint is listed in Details.
- [ ] Defines **no** hooks / lifecycle auto-execution — or each hook and its trigger is described in Details.
- [ ] Does **not** require `--dangerously-skip-permissions` / bypass mode — or the reason is in Details and users are warned.
- [ ] Has **no** telemetry and **no** auto-update (`npx …@latest` etc.) — or it is disclosed in Details.
- [ ] `allowed-tools` is scoped (no `Bash(*)` wildcard) — or the wildcard is justified in Details.
- [ ] Does **not** depend on a commercial/paid product or proprietary API to function — or `depends_3rdparty: true` and it is noted in Details.

**Details** (external endpoints / hook behavior / bypass justification / telemetry / commercial dependency — write "None" if nothing to add):

```
None
```

### Validate the claims (mandatory for a skill or suite)

A specific task to give Claude + the exact prompt that demonstrates the skill,
and what a correct result looks like:

```
```

---

## Contributor checklist

- [ ] **I am a human.** The skill may be AI-assisted, but this submission is made by a person who has actually looked at it.
- [ ] One skill per PR; the file is kebab-case `data/skills/<slug>.yml`; unused optional fields are removed.
- [ ] I did **not** hand-edit `README.md` / `README.zh-CN.md` (they are generated).
- [ ] I searched existing entries and open/closed PRs — this is not a duplicate.
- [ ] All links work and are public; the repo is ≥7 days old (first public commit).
- [ ] I ran, or am willing to run, the `evaluate-repository` static check on the repo.
- [ ] I have read the [Contributing guidelines](../blob/main/CONTRIBUTING.md) and agree to the [Code of Conduct](../blob/main/CODE_OF_CONDUCT.md).
