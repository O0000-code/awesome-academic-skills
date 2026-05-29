#!/usr/bin/env python3
"""Generate README.md and README.zh-CN.md from data/skills/*.yml + config.yaml.

v2 (R3 redesign) — a monochrome Swiss/shadcn, deeply-hierarchical, terse index.

The architecture is verified against the LIVE awesome-lint 2.3.0 ruleset (read from
`node_modules/awesome-lint/rules/*.js`, not summaries):

  * There is NO heading-depth rule. `## <super-group>` (H2) -> `### <category>` (H3)
    -> entry bullets is valid (awesome-selfhosted ships exactly this at 295k stars).
  * The strict `## Contents` TOC validator (single-list, <=2 nesting, 1:1 heading
    match) ONLY fires when a depth-2 heading whose text is exactly `Contents` exists.
    We name the nav `## Table of contents` (selfhosted's proven choice), so that
    rule is a no-op and a NESTED 2-level TOC (super-group -> category) is free-form
    and lint-clean. The manifesto still wants a TOC, so we keep one.
  * `list-item.js`: the link must be followed by a ` - ` (ASCII space-hyphen-space)
    separator — en-dash/em-dash separators ERROR. A LEADING `inlineCode` tag before
    the link is fine (the validator finds the link-followed-by-dash regardless of a
    preceding tag; only a leading *text* node skips validation). A list item must
    END in `.`/`!`/`?`/`…` or an allowed suffix node (a trailing bare `inlineCode`
    tag is NOT allowed), so every bullet terminates in a final `.` after its tags.
  * `double-link.js`: a given link target (external URL or `#hash`) may appear only
    ONCE document-wide; only secondary links inside one item's description are exempt.
    So an entry's link lives in exactly one place (its category bullet); the nested
    TOC links to category HEADINGS (`#slug`), each used once.
  * `license.js`: no heading whose text is `License`. License is a per-entry tag and
    a mono header badge. `no-ci-badge.js`: no CI/build badge.
  * Emphasis uses `*`, never `_`. Tables are pipe-aligned.

Each list line / table row is rendered to a COMPLETE, whitespace-correct string in
Python; the Jinja2 templates only lay out document structure.

Capability disclosure (replaces v1's dishonest "human-reviewed" ✅ and the later
analyzed/listed verdict): each entry's leading tags come from its own `security:`
block (net / hooks / bypass), surfaced as facts by the open ASDF framework. We NEVER
render "human-reviewed", a green check, or a safety verdict, regardless of an entry's
legacy `trust_tier`/`security_review` fields.

Usage:
  python scripts/generate_readme.py            # write both READMEs
  python scripts/generate_readme.py --check     # render in-memory, exit 1 on drift
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import data as D  # noqa: E402

from jinja2 import Environment, FileSystemLoader, StrictUndefined  # noqa: E402


# --------------------------------------------------------------------------
# Anchors — GitHub renders headings to slugs via `github-slugger`: lowercase,
# strip ASCII punctuation (and some unicode), spaces -> '-'. Our headings are
# plain ASCII text (NO emoji in v2), so slugging is the simple word/space/hyphen
# case. We keep word chars, spaces, and hyphens; drop everything else; spaces ->
# '-' (consecutive separators collapse the way github-slugger produces them, e.g.
# `Reading, Summarization & Q&A` -> `reading-summarization--qa`).
# --------------------------------------------------------------------------
_VS16 = "️"
_KEEP = re.compile(r"[^\w \-]", re.UNICODE)

# CJK-flanked space collapser (zh output only): YAML folded scalars insert a literal
# space at each fold; between two wide glyphs that space is a rendering defect. Only a
# run of spaces whose BOTH neighbours are wide glyphs is collapsed; spaces touching
# ASCII/Latin/emoji are preserved (so `技能 / agent`, `Claude / Agent` stay intact).
_CJK = r"[　-〿㐀-䶿一-鿿＀-￯—‘’“”…]"
_CJK_SPACE = re.compile(rf"(?<={_CJK}) +(?={_CJK})")


def gh_anchor(text: str) -> str:
    text = text.replace(_VS16, "")
    text = text.lower()
    text = _KEEP.sub("", text)            # drop ASCII punct + symbols
    text = text.replace("_", "")          # github-slugger also drops underscores
    text = re.sub(r" ", "-", text)        # spaces -> '-' (consecutive -> '--')
    return text


# --------------------------------------------------------------------------
# Loads framework/analysis.yml — the disclosure cross-check map (per slug:
# {disclosure_mismatch: bool}). Drives the `⚠ disclosure` capability tag. Absent /
# malformed -> {} (no flags). We IGNORE any legacy `trust_tier`/`security_review`
# fields — they encoded the dishonest "reviewed" claim the disclosure model removed.
# --------------------------------------------------------------------------
def load_analysis() -> dict:
    path = os.path.join(D.REPO_ROOT, "framework", "analysis.yml")
    if not os.path.exists(path):
        return {}
    try:
        loaded = D.load_yaml(path)
    except Exception:  # noqa: BLE001 — a malformed framework file must not break the index
        return {}
    return loaded if isinstance(loaded, dict) else {}


def render_capability_tags(entry: dict, cfg: dict, analysis: dict = None) -> str:
    """Objective capability tags from the entry's own disclosure block — the honest,
    script-reliable facts (NOT a severity verdict). We dropped the analyzed/listed
    label because its severity bands were noisy/false-positive-prone; a flat factual
    disclosure ('this skill makes network calls / has hooks / needs bypass') is what a
    static reader can state without overclaiming. Tags render as terse mono code spans.

      `net`     — makes network calls beyond the Anthropic API
      `hooks`   — defines lifecycle hooks that run automatically
      `bypass`  — needs --dangerously-skip-permissions (rare; worth knowing)
      `⚠ disclosure` — the author's declaration disagrees with what the code shows
                       (e.g. declared no-network but network calls are present)

    An entry with none of these renders no capability tag (it's a plain local skill).
    """
    sec = entry.get("security") or {}
    tags = []
    if sec.get("makes_network_calls"):
        tags.append("`net`")
    if sec.get("has_hooks"):
        tags.append("`hooks`")
    if sec.get("requires_bypass_permissions"):
        tags.append("`bypass`")
    # Honesty cross-check: the declared block says scoped/no-network/no-hooks but the
    # recorded inferred facts (analysis.yml discrepancies) disagree -> a neutral flag.
    rec = (analysis or {}).get(entry.get("slug", "")) if analysis else None
    if isinstance(rec, dict) and rec.get("disclosure_mismatch"):
        tags.append("`⚠ disclosure`")
    return " ".join(tags)


# --------------------------------------------------------------------------
# Per-entry tag helpers. Order on an entry: LEADING `Type` (before the link),
# then trailing `License` and the analysis marker after the description period.
# --------------------------------------------------------------------------
def type_label(entry: dict, cfg: dict) -> str:
    """The leading monochrome tag. Skills-only scope: a plain `skill` carries NO tag
    (the list is all skills — the tag would be noise on every line). Only the
    *distinguishing* types are tagged: `Suite` (a multi-skill repo), `Plugin`, `List`."""
    t = entry.get("type", "")
    if t == "skill":
        return ""
    return cfg["legends"]["type"]["values"].get(t, t)


def stage_label(entry: dict, cfg: dict) -> str:
    return cfg["legends"]["stage"]["values"].get(
        entry.get("lifecycle_stage", ""), entry.get("lifecycle_stage", "")
    )


def localized(d: dict, key: str, lang: str, default: str = ""):
    """Prefer the `<key>_zh` variant in zh mode, fall back to the base key.

    EN mode always uses the base key. Lists are returned as-is; scalar text is stripped.
    """
    if lang == "zh":
        val = d.get(f"{key}_zh")
        if val is None or (isinstance(val, str) and not val.strip()):
            val = d.get(key)
    else:
        val = d.get(key)
    if val is None:
        return default
    if isinstance(val, str):
        return val.strip()
    return val


def description_for(entry: dict, lang: str) -> str:
    """EN: `description`. zh: `description_zh` if present, else EN.

    The terse one-clause README line. The fuller `description_long` (when W2 splits
    it out) is reserved for the companion site and is NOT rendered here.
    """
    return localized(entry, "description", lang) or (entry.get("description") or "").strip()


def _terminate(desc: str) -> str:
    """Ensure the description clause ends in sentence punctuation (incl. CJK stops)."""
    desc = desc.rstrip()
    if desc and desc[-1] not in ".!?…。！？":
        desc += "."
    return desc


def render_bullet(entry: dict, cfg: dict, analysis: dict, lang: str) -> str:
    r"""A category-body bullet — the ONLY place the entry's external URL appears.

    LOCKED v3 format (skills-only — plain skills carry no tag, only Suite/Plugin/List do;
    author credited in-description; lint-clean — primary link followed by ` - `, the author
    link sits INSIDE the description so double-link.js exempts it, line ends in `.`):
      ``- [name](url) - by [author](author_url). One specific clause. `License` · analyzed.``
      ``- `Suite` [name](url) - by [author](author_url). Description. `License` · listed.``
    """
    type_tag = type_label(entry, cfg)
    desc = _terminate(description_for(entry, lang))
    license_ = (entry.get("license") or "").strip()
    marker = render_capability_tags(entry, cfg, analysis)

    lead = f"`{type_tag}` " if type_tag else ""
    by_word = "作者" if lang == "zh" else "by"
    author = (entry.get("author") or "").strip()
    author_url = (entry.get("author_url") or "").strip()

    # LOCKED v4 layout (owner-chosen): a two-line bullet. Line 1 is the SIGNAL row —
    #   `Type` [name](url) - by [author](url) · `License` · marker
    # then a hard <br> break, and line 2 is the description, visually indented under
    # the name. The link is immediately followed by ` - ` (list-item rule); the author
    # link sits in the description zone so double-link.js exempts repeats; `html` (<br>)
    # is an allowed description node; the line still ends in sentence punctuation.
    credit = f"{by_word} [{author}]({author_url})" if author and author_url else ""
    meta_bits = []
    if credit:
        meta_bits.append(credit)
    if license_:
        meta_bits.append(f"`{license_}`")
    if marker:
        meta_bits.append(marker)
    signal = " · ".join(meta_bits)

    # `- [name](url) - <signal>.<br>Description.`  The trailing period after the signal
    # row keeps a valid sentence-terminated segment; <br> is inline html; the final
    # description is terminated by `_terminate`.
    head = f"- {lead}[{entry['name']}]({entry['source_url']}) - "
    if signal:
        return f"{head}{signal}.<br>{desc}"
    return f"{head}{desc}"


def fmt_stars(n) -> str:
    if not isinstance(n, int):
        return "—"
    if n >= 1000:
        return f"{n / 1000:.1f}k".replace(".0k", "k")
    return str(n)


# --- Pipe-aligned tables (remark-lint table-pipe-alignment / table-cell-padding) ---
def _vis_len(text: str) -> int:
    """Code-point length — remark-lint counts code points, not display columns, so
    the separator row matches the linter's expectation (wide-glyph visual misalignment
    is cosmetic; lint passes)."""
    return len(text)


def render_table(headers: list[str], rows: list[list[str]], aligns: list[str]) -> list[str]:
    ncol = len(headers)
    cells = [headers] + rows
    widths = [0] * ncol
    for row in cells:
        for i in range(ncol):
            widths[i] = max(widths[i], _vis_len(row[i]))

    def pad(text: str, i: int) -> str:
        gap = widths[i] - _vis_len(text)
        a = aligns[i]
        if a == "right":
            return " " * gap + text
        if a == "center":
            left = gap // 2
            return " " * left + text + " " * (gap - left)
        return text + " " * gap

    def sep(i: int) -> str:
        a = aligns[i]
        w = widths[i]
        if a == "right":
            return "-" * (w - 1) + ":"
        if a == "center":
            return ":" + "-" * (w - 2) + ":"
        return "-" * w

    lines = ["| " + " | ".join(pad(headers[i], i) for i in range(ncol)) + " |",
             "| " + " | ".join(sep(i) for i in range(ncol)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(pad(row[i], i) for i in range(ncol)) + " |")
    return lines


def suite_table(entries: list[dict], cfg: dict, analysis: dict, lang: str, labels: dict) -> list[str]:
    """The one comparison table (Skill Suites). Type is uniform (Suite) so the last
    column shows the objective capability tags (net/hooks/bypass) instead — consistent
    with the bullets; the table earns its place via ★ / #Skills / Best-for."""
    headers = [labels["suite"], "★", labels["skills"], labels["best_for"], labels["caps"]]
    aligns = ["left", "right", "right", "left", "left"]
    rows = []
    for e in entries:
        name = f"[{e['name']}]({e['source_url']})"
        stars = fmt_stars(e.get("stargazers_count"))
        nsk = e.get("skills_count")
        nsk = str(nsk) if isinstance(nsk, int) else "—"
        best = description_for(e, lang).replace("|", "\\|")
        best = best.rstrip(" .。") + ("。" if lang == "zh" and best and best[-1] not in ".。" else "")
        caps = render_capability_tags(e, cfg, analysis).replace("|", "\\|") or "—"
        rows.append([name, stars, nsk, best, caps])
    if not rows:
        rows.append([labels["empty"], "—", "—", "—", "—"])
    return render_table(headers, rows, aligns)


# --------------------------------------------------------------------------
# Build the template context
# --------------------------------------------------------------------------
def order_key(e: dict):
    """Deterministic in-category ordering (D5 LOCKED): ALPHABETICAL, case-insensitive
    by display name, with the slug as a stable tiebreaker. Neutral, auditable, and
    removes any self-preferencing lever (the owner's skills sort like everyone's)."""
    return (e.get("name", "").lower(), e.get("slug", ""))


TABLE_LABELS = {
    "en": {"suite": "Suite", "skills": "Skills", "best_for": "Best for",
           "caps": "Runs", "empty": "No suites listed yet."},
    "zh": {"suite": "套件", "skills": "技能数", "best_for": "最适合",
           "caps": "运行", "empty": "暂无套件。"},
}

# Localized fixed section names (must match the headings the templates emit).
# NOTE: the TOC heading is literally `Contents` (EN) so awesome-lint's strict
# `toc.js` validator fires — which is what we WANT: it validates the nested TOC as
# a TOC (depth-0 list item <-> H2, depth-1 <-> H3, exactly our super-group/category
# shape) AND excludes the TOC from `list-item.js` entry-link validation. (Verified
# empirically against awesome-lint 2.3.0; the alternative `Table of contents` name
# leaves the TOC's `#hash` links to be misvalidated as entry URLs and FAILS.)
# `toc.js` then requires EVERY non-denylisted H2 to appear in the TOC in order, so
# the below-fold sections are TOC items too (Contributing is auto-denylisted).
# The zh README is not linted, but mirrors the structure; its TOC heading is 目录.
LOCALIZED_SECTIONS = {
    "en": {
        "toc": "Contents",
        "at_a_glance": "At a glance",
        "latest": "Recently updated",
        "how_to_use": "How to use this list",
        "curation": "What gets listed",
        "about": "Curation, neutrality & security",
        "contributing": "Contributing",
    },
    "zh": {
        "toc": "目录",
        "at_a_glance": "速览",
        "latest": "最近更新",
        "how_to_use": "如何使用本列表",
        "curation": "收录标准",
        "about": "策展、中立性与安全",
        "contributing": "参与贡献",
    },
}


def _suites_first(entries: list[dict]) -> list[dict]:
    """Order entries SUITES first, then everything else; alphabetical within each tier
    (D5 neutral ordering). The owner's rule: a suite wedged among single skills creates
    needless cognitive cost, so suites lead each (sub)category."""
    suites = [e for e in entries if e.get("type") == "suite"]
    rest = [e for e in entries if e.get("type") != "suite"]
    suites.sort(key=order_key)
    rest.sort(key=order_key)
    return suites + rest


def _build_subcats(entries: list[dict], sub_order: list, cfg: dict,
                   analysis: dict, lang: str) -> list[dict]:
    """Group a category's entries under its ordered subcategories (H4). Suites lead each
    subcategory. Subcategories render in the configured order; any entry whose
    `subcategory` is missing/unknown falls into a trailing 'More' bucket (defensive)."""
    order_names = [s["name"] for s in sub_order]
    buckets: dict[str, list[dict]] = {n: [] for n in order_names}
    extra: list[dict] = []
    for e in entries:
        sc = (e.get("subcategory") or "").strip()
        (buckets[sc] if sc in buckets else extra).append(e)
    out = []
    for s in sub_order:
        es = buckets.get(s["name"], [])
        if not es:
            continue
        out.append({
            "display": (s.get("name_zh") or s["name"]) if lang == "zh" else s["name"],
            "anchor": gh_anchor((s.get("name_zh") or s["name"]) if lang == "zh" else s["name"]),
            "bullets": [render_bullet(e, cfg, analysis, lang) for e in _suites_first(es)],
        })
    if extra:
        label = "更多" if lang == "zh" else "More"
        out.append({
            "display": label, "anchor": gh_anchor(label),
            "bullets": [render_bullet(e, cfg, analysis, lang) for e in _suites_first(extra)],
        })
    return out


def build_context(cfg: dict, entries: list[dict], lang: str) -> dict:
    today = _dt.date.today().isoformat()
    labels = TABLE_LABELS[lang]
    sec = LOCALIZED_SECTIONS[lang]
    analysis = load_analysis()

    by_category: dict[str, list[dict]] = {}
    for e in entries:
        by_category.setdefault(e.get("category", ""), []).append(e)
    for cat in by_category:
        by_category[cat].sort(key=order_key)

    # ----- super-group -> category structure (the deep hierarchy) -----
    # `display` is the localized heading text (label_zh / category_zh in zh, else the
    # English key). The anchor is the github-slug of THAT display text, so the zh
    # README's TOC links resolve against its Chinese headings (the EN file slugs the
    # English headings). `category` stays the English enum key (data join + counts).
    groups = []           # [{label, display, blurb, anchor, categories:[...]}]
    flat_categories = []  # category dicts in document order (for counts/latest)
    for grp in cfg["super_groups"]:
        g_display = localized(grp, "label", lang) or grp["label"]
        g = {
            "label": grp["label"],
            "display": g_display,
            "blurb": localized(grp, "blurb", lang),
            "anchor": gh_anchor(g_display),
            "categories": [],
        }
        for c in grp["categories"]:
            c_display = localized(c, "category", lang) or c["category"]
            cat = {
                "category": c["category"],
                "display": c_display,
                "group": grp["label"],
                "anchor": gh_anchor(c_display),
                "blurb": localized(c, "blurb", lang),
                "render": c.get("render", "bullets"),
                "entries": by_category.get(c["category"], []),
            }
            cat["count"] = len(cat["entries"])
            if cat["render"] == "table":
                cat["table_lines"] = suite_table(cat["entries"], cfg, analysis, lang, labels)
                cat["bullets"] = []
                cat["subcats"] = []
            else:
                cat["table_lines"] = []
                # Second-level taxonomy: if this category has a configured ordered
                # subcategory list, group entries under `#### <subcategory>` (suites
                # first within each). Else render a flat bullet list as before.
                sub_order = (cfg.get("subcategories", {}) or {}).get(c["category"])
                if sub_order:
                    cat["bullets"] = []
                    cat["subcats"] = _build_subcats(
                        cat["entries"], sub_order, cfg, analysis, lang
                    )
                else:
                    cat["subcats"] = []
                    cat["bullets"] = [render_bullet(e, cfg, analysis, lang)
                                      for e in _suites_first(cat["entries"])]
            g["categories"].append(cat)
            flat_categories.append(cat)
        g["count"] = sum(c["count"] for c in g["categories"])
        groups.append(g)

    # ----- nested TOC: super-group (H2, depth-0) -> category (H3, depth-1) -----
    # PLUS the below-fold sections as trailing flat depth-0 items. `toc.js` requires
    # EVERY non-denylisted H2 in document order, so the TOC item TEXT must equal each
    # heading's text exactly and the order must match the template's H2 order:
    #   [6 super-groups], At a glance, Recently updated, How to use, What gets listed,
    #   <about>.  `Contributing` is denylisted and MUST NOT appear here.
    toc_groups = [
        {
            "label": g["display"],
            "anchor": g["anchor"],
            "children": [{"label": c["display"], "anchor": c["anchor"]} for c in g["categories"]],
        }
        for g in groups
    ]
    # The trailing below-fold H2 sections, in the exact order the template emits them.
    toc_trailing = [
        {"label": sec["at_a_glance"], "anchor": gh_anchor(sec["at_a_glance"]), "children": []},
        {"label": sec["latest"], "anchor": gh_anchor(sec["latest"]), "children": []},
        {"label": sec["how_to_use"], "anchor": gh_anchor(sec["how_to_use"]), "children": []},
        {"label": sec["curation"], "anchor": gh_anchor(sec["curation"]), "children": []},
        {"label": sec["about"], "anchor": gh_anchor(sec["about"]), "children": []},
    ]

    # ----- "At a glance" dashboard rows (super-group · #categories · #entries) -----
    glance_rows = [
        [g["display"], str(len(g["categories"])), str(g["count"])] for g in groups
    ]
    glance_labels = ({"group": "Lifecycle stage", "cats": "Categories", "count": "Skills"}
                     if lang == "en" else
                     {"group": "生命周期阶段", "cats": "分类", "count": "技能数"})
    glance_table = render_table(
        [glance_labels["group"], glance_labels["cats"], glance_labels["count"]],
        glance_rows + [(("Total" if lang == "en" else "合计"),
                        str(len(flat_categories)), str(len(entries)))],
        ["left", "right", "right"],
    )

    # ----- "Recently updated" (newest by updated_at / current_release date) -----
    def freshness_key(e):
        d = e.get("updated_at") or (e.get("current_release") or {}).get("published_at")
        return d or ""

    latest_n = cfg.get("render", {}).get("latest_additions_count", 5)

    def _repo_key(e):
        m = re.search(r"github\.com/([^/]+/[^/]+)", e.get("source_url", ""))
        return m.group(1) if m else e.get("slug", "")

    _seen, latest_sorted = set(), []
    for e in sorted(entries, key=freshness_key, reverse=True):
        rk = _repo_key(e)
        if rk in _seen:
            continue
        _seen.add(rk)
        latest_sorted.append(e)
        if len(latest_sorted) >= latest_n:
            break
    # Bold plain names, no links (the single link lives on the category bullet).
    latest_prose = ", ".join(f"**{e['name']}**" for e in latest_sorted)

    # ----- type-vocabulary legend (closed set, one line) -----
    type_order = cfg["legends"]["type"].get("order", list(cfg["legends"]["type"]["values"]))
    type_legend_bits = [f"`{cfg['legends']['type']['values'][k]}`" for k in type_order
                        if k in cfg["legends"]["type"]["values"]]
    type_legend = " · ".join(type_legend_bits)

    # ----- editorial prose (zh-aware) -----
    ed_base = cfg["editorial"]
    ed_zh = cfg.get("editorial_zh", {}) if lang == "zh" else {}

    def ed_field(key: str):
        if lang == "zh":
            val = ed_zh.get(key)
            if val is not None and (not isinstance(val, str) or val.strip()):
                return val.strip() if isinstance(val, str) else val
        base = ed_base.get(key)
        return base.strip() if isinstance(base, str) else base

    list_sep, list_end = ("；", "。") if lang == "zh" else ("; ", ".")

    def join_clean(items):
        cleaned = [s.rstrip("。！？；.;") for s in (items or [])]
        return list_sep.join(cleaned) + list_end

    curation_included_prose = join_clean(ed_field("curation_included"))
    curation_excluded_prose = join_clean(ed_field("curation_excluded"))

    ED_SCALAR_FIELDS = (
        "tagline", "how_to_use_intro", "lifecycle_flow", "security_note",
        "analysis_note", "neutrality_clause", "contributing_pointer",
    )
    ed_ctx = {k: ed_field(k) for k in ED_SCALAR_FIELDS}
    ed_ctx["hero_lines"] = ed_field("hero_lines") or []

    return {
        "lang": lang,
        "is_zh": lang == "zh",
        "cfg": cfg,
        "site": cfg["site"],
        "ed": ed_ctx,
        "updated": today,
        "updated_dotted": today.replace("-", "."),   # 2026.05.29 (micro-typography)
        "skills_count": len(entries),
        "categories_count": len(flat_categories),
        "groups": groups,
        "toc_groups": toc_groups,
        "toc_trailing": toc_trailing,
        "glance_table": glance_table,
        "show_glance": cfg.get("render", {}).get("show_at_a_glance_table", True),
        "latest_prose": latest_prose,
        "type_legend": type_legend,
        "analysis_legend": localized(cfg["analysis"], "legend", lang),
        "curation_included_prose": curation_included_prose,
        "curation_excluded_prose": curation_excluded_prose,
        "sec": sec,
    }


# --------------------------------------------------------------------------
# Render
# --------------------------------------------------------------------------
def make_env() -> Environment:
    return Environment(
        loader=FileSystemLoader(D.TEMPLATES_DIR),
        undefined=StrictUndefined,
        trim_blocks=True,
        lstrip_blocks=True,
        keep_trailing_newline=True,
    )


def render(lang: str, cfg: dict, entries: list[dict]) -> str:
    env = make_env()
    tmpl = env.get_template("README.zh-CN.md.j2" if lang == "zh" else "README.md.j2")
    text = tmpl.render(**build_context(cfg, entries, lang))
    text = re.sub(r"[ \t]+\n", "\n", text)       # strip trailing spaces
    text = re.sub(r"\n{3,}", "\n\n", text)        # collapse 3+ blanks
    if lang == "zh":
        text = _CJK_SPACE.sub("", text)
    text = text.rstrip("\n") + "\n"               # exactly one trailing newline
    return text


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate README.md + README.zh-CN.md")
    ap.add_argument("--check", action="store_true", help="render and diff; exit 1 on drift")
    args = ap.parse_args()

    cfg = D.load_config()
    entries = D.load_entries()

    drift = False
    for lang, path in (("en", D.README_EN), ("zh", D.README_ZH)):
        new_text = render(lang, cfg, entries)
        if args.check:
            old = ""
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as fh:
                    old = fh.read()
            if old != new_text:
                drift = True
                D.eprint(f"DRIFT: {os.path.basename(path)} is out of date — run `make generate`.")
        else:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new_text)
            print(f"wrote {os.path.relpath(path, D.REPO_ROOT)} ({len(entries)} entries)")

    if args.check and drift:
        return 1
    if args.check:
        print("generate --check: READMEs are up to date.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
