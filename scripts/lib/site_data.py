"""Site data layer — shared between the README generator and the companion site.

`web/scripts/gen_data.py` calls `build_site_model()` to emit `web/src/data.json`,
which drives the React companion site (`web/` → built to `docs/`). It reads the
SAME data layer the README is generated from (`data/skills/*.yml` +
`framework/analysis.yml` + `config.yaml`), so the site can never drift from the
README. This module is the join: it loads the raw entries via `lib.data`, attaches
the disclosure cross-check to each, normalizes the fields the site renders, and
exposes the lifecycle taxonomy (super-group -> category) in document order.

Pure stdlib + PyYAML (same dependency surface as the rest of `scripts/`).

Honesty contract (mirrors the README generator):
  * Entries carry objective capability tags (net / hooks / bypass) from their own
    `security:` block, plus a disclosure-mismatch flag from `framework/analysis.yml`.
    We NEVER emit "human-reviewed", a green check, or a safety verdict, and we ignore
    any legacy `trust_tier` / `security_review` fields.
  * The tags are disclosed facts, NOT a safety rating.
"""

from __future__ import annotations

import os
import re
from typing import Any

from . import data as D

# The owner's report uses the GitHub blob path for files that GitHub Pages cannot
# serve (anything outside /docs). The companion site lives under /docs, so a relative
# link to ../framework/... would 404 on Pages. We link analysis reports to the
# absolute github.com blob URL instead (the spec's explicit instruction).
GITHUB_BLOB_BASE = "https://github.com/O0000-code/awesome-academic-skills/blob/main"


def _repo_slug_from_url(repo_url: str) -> str:
    """Extract `owner/repo` from a GitHub repo URL, for the blob base."""
    m = re.search(r"github\.com/([^/]+/[^/]+?)(?:\.git)?/?$", repo_url or "")
    return m.group(1) if m else "O0000-code/awesome-academic-skills"


def load_analysis() -> dict:
    """Load `framework/analysis.yml` (ASDF output). Absent/malformed -> {} (all listed)."""
    path = os.path.join(D.REPO_ROOT, "framework", "analysis.yml")
    if not os.path.exists(path):
        return {}
    try:
        loaded = D.load_yaml(path)
    except Exception:  # noqa: BLE001 — a malformed framework file must not break the site
        return {}
    return loaded if isinstance(loaded, dict) else {}


def _analysis_for(slug: str, analysis: dict) -> dict:
    """Disclosure cross-check for a slug. The old analyzed/listed severity verdict was
    removed (false-positive-prone); analysis.yml now records only whether the author's
    declaration disagrees with the code (`disclosure_mismatch`)."""
    rec = analysis.get(slug)
    dm = bool(rec.get("disclosure_mismatch")) if isinstance(rec, dict) else False
    return {"disclosure_mismatch": dm}


# License strings that read as a caution flag (non-OSI / restrictive / absent).
# These get a subtle monochrome "caution" treatment on the site (NOT color — a
# small dotted ring), mirroring the README convention that renders them verbatim.
_CAUTION_LICENSE_RE = re.compile(
    r"(no\s*license|proprietary|nc\b|non-?commercial|licenseref|noassertion)",
    re.IGNORECASE,
)


def is_caution_license(license_: str) -> bool:
    if not license_:
        return True
    return bool(_CAUTION_LICENSE_RE.search(license_))


def normalize_license(raw: str) -> str:
    """The loader already strips trailing `# comments` from scalars; just tidy."""
    return (raw or "").strip()


def stage_label(stage: str, cfg: dict) -> str:
    return cfg["legends"]["stage"]["values"].get(stage, stage or "")


def type_label(t: str, cfg: dict) -> str:
    return cfg["legends"]["type"]["values"].get(t, t or "")


def _subcat_zh(category, subcategory, cfg: dict) -> str:
    """The Chinese label for an entry's subcategory, looked up in config's
    `subcategories` map; falls back to the English subcategory (or empty)."""
    sub = (subcategory or "").strip()
    if not sub:
        return ""
    for sc in (cfg.get("subcategories", {}) or {}).get((category or "").strip(), []):
        if sc.get("name") == sub:
            return sc.get("name_zh") or sub
    return sub


def _security_flags(sec: dict) -> dict:
    """A terse, honest summary of the self-declared security disclosure.

    Returns booleans the site can render as small mono chips (network / hooks /
    bypass / 3rd-party). These are AUTHOR DECLARATIONS surfaced verbatim — the site
    states that plainly; it is not a verdict.
    """
    sec = sec or {}
    return {
        "network": bool(sec.get("makes_network_calls")),
        "hooks": bool(sec.get("has_hooks")),
        "bypass": bool(sec.get("requires_bypass_permissions")),
        "telemetry": bool(sec.get("telemetry")),
        "third_party": bool(sec.get("depends_3rdparty")),
        "endpoints": [str(e) for e in (sec.get("network_endpoints") or [])],
    }


def build_entry(raw: dict, cfg: dict, analysis: dict) -> dict:
    """Project one raw skill YAML into the flat record the site renders.

    Bilingual: both EN and zh strings travel to the client so the language toggle is
    instant (no reload). Falls back to EN when a zh variant is missing.
    """
    slug = (raw.get("slug") or "").strip()
    typ = (raw.get("type") or "").strip()
    stage = (raw.get("lifecycle_stage") or "").strip()
    license_ = normalize_license(raw.get("license") or "")
    info = _analysis_for(slug, analysis)

    def _txt(key: str) -> str:
        v = raw.get(key)
        return v.strip() if isinstance(v, str) else (v or "")

    desc_zh = _txt("description_zh") or _txt("description")
    desc_long_zh = _txt("description_zh_long") or _txt("description_long") or desc_zh

    stars = raw.get("stargazers_count")
    return {
        "slug": slug,
        "name": (raw.get("name") or "").strip(),
        "url": (raw.get("source_url") or "").strip(),
        "homepage": (raw.get("homepage_url") or "").strip(),
        "author": (raw.get("author") or "").strip(),
        "author_url": (raw.get("author_url") or "").strip(),
        "type": typ,
        "type_label": type_label(typ, cfg),
        "category": (raw.get("category") or "").strip(),
        "subcategory": (raw.get("subcategory") or "").strip(),
        "subcategory_zh": _subcat_zh(raw.get("category"), raw.get("subcategory"), cfg),
        "stage": stage,
        "stage_label": stage_label(stage, cfg),
        "license": license_,
        "license_caution": is_caution_license(license_),
        # Bilingual text payloads.
        "desc_en": _txt("description"),
        "desc_zh": desc_zh,
        "desc_long_en": _txt("description_long") or _txt("description"),
        "desc_long_zh": desc_long_zh,
        # Numbers / meta.
        "stars": stars if isinstance(stars, int) else None,
        "skills_count": raw.get("skills_count") if isinstance(raw.get("skills_count"), int) else None,
        "updated_at": (raw.get("updated_at") or "").strip() or None,
        "archived": bool(raw.get("archived")),
        # Disclosure cross-check: the author's declaration disagrees with the code
        # (a High-band discrepancy). Replaces the old analyzed/listed severity verdict.
        "disclosure_mismatch": bool(info.get("disclosure_mismatch")),
        # Capability disclosure (author-declared, surfaced verbatim as facts — NOT a rating).
        "security": _security_flags(raw.get("security") or {}),
        "tags": [str(t) for t in (raw.get("tags") or [])],
    }


def build_site_model(cfg: dict | None = None) -> dict:
    """The complete model the site template renders.

    Returns:
      {
        meta: {...},                  # title, repo url, counts, generated date
        entries: [entry, ...],        # ALL entries, alphabetical by name (D5)
        groups: [                     # lifecycle taxonomy in document order
          {key, label_en, label_zh, blurb_en, blurb_zh,
           categories: [{key, label_en, label_zh, blurb_en, blurb_zh, render}, ...]},
          ...
        ],
        types: [{key, label, def_en}, ...],     # closed type vocabulary (legend order)
        stages: [{key, label}, ...],            # lifecycle stages in document order
        licenses: [str, ...],                   # distinct licenses present (for filter)
        legends: {...},                         # analysis legend EN/zh + honest framing
      }
    """
    if cfg is None:
        cfg = D.load_config()
    analysis = load_analysis()
    raw_entries = D.load_entries()

    entries = [build_entry(e, cfg, analysis) for e in raw_entries]
    # D5 LOCKED: deterministic ALPHABETICAL by display name (case-insensitive),
    # slug as a stable tiebreaker. Neutral, no self-preferencing lever.
    entries.sort(key=lambda e: (e["name"].lower(), e["slug"]))

    # Lifecycle taxonomy (super-group -> category) in document order, with the
    # stage each category files under (so a stage filter maps to categories).
    groups = []
    stages_seen: list[dict] = []
    stage_keys: set[str] = set()
    for grp in cfg["super_groups"]:
        cats = []
        for c in grp["categories"]:
            st = c.get("stage", "")
            cats.append({
                "key": c["category"],
                "label_en": c["category"],
                "label_zh": c.get("category_zh", c["category"]),
                "blurb_en": (c.get("blurb") or "").strip(),
                "blurb_zh": (c.get("blurb_zh") or c.get("blurb") or "").strip(),
                "stage": st,
                "render": c.get("render", "bullets"),
            })
            if st and st not in stage_keys:
                stage_keys.add(st)
                stages_seen.append({"key": st, "label": stage_label(st, cfg)})
        groups.append({
            "key": grp["label"],
            "label_en": grp["label"],
            "label_zh": grp.get("label_zh", grp["label"]),
            "blurb_en": (grp.get("blurb") or "").strip(),
            "blurb_zh": (grp.get("blurb_zh") or grp.get("blurb") or "").strip(),
            "categories": cats,
        })

    # Type facet — built from the types that ACTUALLY occur in the data (so the
    # filter never shows an empty option), skill first then the distinguishing kinds.
    # NB: this differs on purpose from the README inline-tag/legend rule (which omits
    # `skill`): the site's *filter* still needs a `skill` option (skills are the bulk),
    # even though a skill card shows no type badge.
    tdef = cfg["legends"]["type"]
    present = {e.get("type", "") for e in entries}
    pref = ["skill", "suite", "plugin", "list", "mcp-server", "tool", "template"]
    type_keys = [k for k in pref if k in present] + sorted(present - set(pref) - {""})
    types = [
        {
            "key": k,
            "label": tdef["values"].get(k, k.title()),
            "def_en": tdef.get("defs", {}).get(k, ""),
        }
        for k in type_keys
    ]

    # Distinct licenses actually present (for the license filter), sorted with the
    # caution ones grouped naturally by their verbatim strings.
    licenses = sorted({e["license"] for e in entries if e["license"]})

    # Honest analysis legend (verbatim from config, EN + zh).
    legends = {
        "analysis_en": cfg["analysis"]["legend"],
        "analysis_zh": cfg["analysis"].get("legend_zh", cfg["analysis"]["legend"]),
    }

    repo_url = cfg["site"]["repo_url"]
    n_suites = sum(1 for e in entries if e.get("type") == "suite")
    meta = {
        "title": cfg["site"]["title"],
        "repo_url": repo_url,
        "repo_slug": _repo_slug_from_url(repo_url),
        "awesome_url": cfg["site"].get("awesome_url", "https://awesome.re"),
        "homepage_url": f"https://o0000-code.github.io/awesome-academic-skills/",
        "data_as_of": cfg["site"].get("data_as_of", ""),
        "count_total": len(entries),
        "count_suites": n_suites,
        "count_categories": sum(len(g["categories"]) for g in groups),
        "count_groups": len(groups),
    }

    return {
        "meta": meta,
        "entries": entries,
        "groups": groups,
        "types": types,
        "stages": stages_seen,
        "licenses": licenses,
        "legends": legends,
        # Editorial hero/taglines (bilingual), reused from the README's source.
        "editorial": {
            "tagline_en": cfg["editorial"]["tagline"],
            "tagline_zh": cfg.get("editorial_zh", {}).get("tagline", cfg["editorial"]["tagline"]),
            "hero_en": cfg["editorial"].get("hero_lines", []),
            "hero_zh": cfg.get("editorial_zh", {}).get("hero_lines", cfg["editorial"].get("hero_lines", [])),
            "lifecycle_en": cfg["editorial"].get("lifecycle_flow", ""),
            "lifecycle_zh": cfg.get("editorial_zh", {}).get("lifecycle_flow", cfg["editorial"].get("lifecycle_flow", "")),
        },
    }
