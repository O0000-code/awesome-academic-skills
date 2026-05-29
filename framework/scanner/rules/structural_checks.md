# ASDF structural checks — the non-regex deterministic checks

These are the deterministic checks the scanner runs that are **not** simple
content-pattern matches. They inspect repository *structure* and *config*
(presence of a license, hook declarations, `allowed-tools` scoping, dependency
pinning). They are documented here as readable data so the heuristics are open
and contestable, exactly like `patterns.yml`.

Each row: the check, what triggers it, the severity band of a negative result,
and why it matters. "Negative result" = the condition that produces a finding.

| Check id | What it inspects | Finding condition | Severity | Why it matters |
|---|---|---|---|---|
| `license-present` | `LICENSE` / `LICENSE.*` / `COPYING` / `licen[sc]e*` at repo root | **No** license file found | Medium | An unlicensed skill is legally unsafe to reuse; awesome-list inclusion requires a stated license. (Reported as Info-positive when present.) |
| `allowed-tools-wildcard` | `allowed-tools:` in `SKILL.md` frontmatter / `settings.json` | Contains `Bash(*)` or bare unscoped `Bash` (no `(...)` scope) | High | A `Bash(*)` wildcard grants the skill unrestricted shell — the widest possible execution surface. Should be scoped to specific commands. |
| `hooks-present` | a `hooks:` / `"hooks":` key in a recognised agent-config file (`SKILL.md`, `settings.json`, `plugin.json`, `marketplace.json`, `config.y*ml`, `agent.*`) **or** an agent-config hooks directory (`.claude/hooks/`, `.agent/hooks/`, `.codex/hooks/`, or a top-level `hooks/` that is **not** under a frontend source root) | A genuine Claude/agent lifecycle hook is present | Medium | Hooks execute automatically on tool-lifecycle events — implicit execution the user did not directly invoke. Enumerate triggers. (Escalated to High if a hook file also matches any network-IO pattern.) **Frontend custom-hook directories (`src/hooks/`, `app/hooks/`, React `useFoo` files) are explicitly excluded** — they are not agent lifecycle hooks. |
| `hook-network-io` | files identified as hooks (above) | A hook file also matches a network call (`requests`, `urllib`, `fetch`, `curl`, `http`) | High | A hook that runs automatically **and** makes network calls is the most dangerous implicit surface: silent network IO with no user action. Mandatory manual review. |
| `deny-rules-present` | `settings.json` / config | `"deny"` / `deny:` rules present | Info (positive) | Explicit deny rules are a *defensive* signal — reported as a positive, never a finding. |
| `unpinned-deps` | `requirements.txt`, `package.json`, `pyproject.toml`, etc. | Dependency specs without a pinned version (covered by the `auto-update-latest` pattern) | Medium | Unpinned deps mean a future (possibly compromised) release runs unreviewed. Supply-chain drift. |

## Read-only safety: the symlink guard

The scanner is read-only and must never read outside the clone. It therefore
**never follows a symlink**: symlinked files are skipped, symlinked directories
are not descended into, and any file whose real (symlink-resolved) path escapes
the clone root is refused. This prevents a repo from exfiltrating a sensitive
local file through the scanner — e.g. a committed `creds.txt -> ~/.aws/credentials`
or a `data/ -> /etc` directory symlink — which would otherwise be read and
reported as if it were repository content.

## Context downgrades (recorded, never silent)

- **Documentation files** (`.md`, `.markdown`, `.txt`, `.rst`) and **example-data
  files** (paths under `examples/`, `samples/`, `fixtures/`, `testdata/`,
  `corpus/`, `templates/`, `__snapshots__/`, `cassettes/`, …): a dangerous
  *string* here is almost always text being shown, not code being run. For the
  high-impact "scary" categories (credential-path, destructive, exfil,
  reverse-shell, decode-then-exec, dangerous-powershell) the finding is
  **downgraded two bands** (Critical → Low) so e.g. a `/etc/passwd` string in
  textbook prose cannot land at High; other categories drop one band.
- **Commented-out code** inside scripts (`# …`, `// …`, `* …`, `<!-- … -->`) is
  not an execution sink, so the execution/destructive categories do not fire on a
  commented line.
- **`dangerous-eval-exec`** does not fire on a function/method *definition* or a
  class named `Eval`/`Exec` (`def eval(`, `async def eval(`, `class Eval(`) — a
  definition is the thing being defined, not a call.
- **`hidden-unicode`** in a normal quoted string literal assigned to a
  descriptively-named variable (a deliberate ZWSP feature) is down-weighted to
  Low; a zero-width char inside an identifier/comment keeps full weight.

All downgrades are recorded in the per-entry report (`downgraded_from` + reason),
never silently dropped.

## How a check becomes a report finding

1. The scanner walks the repo read-only (skipping `.git`, `node_modules`, `.venv`, vendored dirs, symlinks, and files > 2 MB).
2. Pattern rules (`patterns.yml`) match against each text file's content.
3. Structural checks (this file) inspect presence/config as above.
4. Each finding is emitted with `{severity, category, file, line, snippet}`.
5. The scanner cross-checks the entry's **declared** `security:` block (Stage 0) against what it **inferred** (Stage 1) and emits a **Discrepancies** list: `makes_network_calls: false` declared but a network call found (High), `has_hooks: false` declared but a hook found (High), `allowed_tools_scoped: true` declared but `Bash(*)` / unscoped `Bash` inferred (High), `telemetry: false` declared but a telemetry endpoint found (Medium), and declared-vs-seen endpoint gaps (Low).
6. The **top severity** across all findings sets the entry's band — an advisory triage signal in the scan output. It no longer drives a published label: the list shows capability tags (`net` / `hooks` / `bypass`), not a verdict.

## Contesting a check

Every check here and every pattern in `patterns.yml` is open data. To contest a
false positive or propose a new check: open an issue/PR against this folder. See
`../../VALIDATION.md` for the contest channel and `../../README.md` for the
honest-limits statement.
