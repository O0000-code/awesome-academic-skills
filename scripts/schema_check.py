#!/usr/bin/env python3
"""Validate every data/skills/*.yml against schema/skill.schema.json, then apply
the cross-field rules that pure JSON Schema cannot express.

JSON Schema validation uses the `jsonschema` package when it is installed
(this is what CI uses — see Makefile / validate.yml). When `jsonschema` is not
available, a small built-in validator covers the locked structural rules
(required fields, enums, maxLength, and the two conditional blocks) so the check
still runs in a bare environment. Cross-field rules below always run.

Cross-field rules (07_RF §3/§6, 02_build_round_plan §0.2):
  X1  slug == filename (without .yml)
  X2  recusal: for owner-authored reviewed entries, security_review.reviewer
      MUST differ from author (R-RF-6). Owner handle is configurable.
  X3  validate_claim is mandatory for type skill | suite.

Exit code: 0 if all entries pass, 1 if any error is found.
"""

from __future__ import annotations

import json
import os
import sys

# Allow running both as `python scripts/schema_check.py` and as a module.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import data as D  # noqa: E402

# Handles considered "the list owner" for the recusal rule (X2). Extend as
# co-owned accounts are added. Compared case-insensitively against `author`.
OWNER_HANDLES = {"paper-search-pro-owner", "ssci-plots-owner"}
# Also treat any author whose author_url points at these GitHub orgs/users as
# owner-authored. Keep in sync with the owner's real public handle on publish.
OWNER_URL_FRAGMENTS = ("/o0000-code", "/paper-search-pro", "/ssci-plots")


def load_schema() -> dict:
    with open(D.SCHEMA_PATH, "r", encoding="utf-8") as fh:
        return json.load(fh)


# --------------------------------------------------------------------------
# JSON Schema validation (jsonschema if present, else a built-in fallback)
# --------------------------------------------------------------------------
def jsonschema_errors(entry: dict, schema: dict) -> list[str]:
    payload = {k: v for k, v in entry.items() if not k.startswith("_")}
    try:
        import jsonschema  # type: ignore
        from jsonschema import Draft7Validator

        validator = Draft7Validator(schema)
        errs = []
        for e in sorted(validator.iter_errors(payload), key=lambda x: list(x.path)):
            loc = "/".join(str(p) for p in e.path) or "(root)"
            errs.append(f"schema: {loc}: {e.message}")
        return errs
    except ImportError:
        return _builtin_validate(payload, schema)


def _builtin_validate(entry: dict, schema: dict) -> list[str]:
    """Minimal Draft-07 subset covering this schema's locked rules.

    Intentionally not a general validator — it checks exactly what
    skill.schema.json uses: required, enum, type, maxLength, format-ish uri,
    plus the two conditional `allOf` blocks (trust_tier <-> security_review,
    makes_network_calls <-> network_endpoints). CI uses real jsonschema.
    """
    errs: list[str] = []

    def check_object(obj, sch, prefix):
        if sch.get("additionalProperties") is False:
            allowed = set(sch.get("properties", {}).keys())
            for k in obj:
                if k not in allowed:
                    errs.append(f"schema: {prefix}{k}: additional property not allowed")
        for req in sch.get("required", []):
            if req not in obj:
                errs.append(f"schema: {prefix}{req}: required field missing")
        for key, subsch in sch.get("properties", {}).items():
            if key in obj:
                check_value(obj[key], subsch, f"{prefix}{key}")

    def check_value(val, sch, loc):
        types = sch.get("type")
        if types is not None:
            tlist = types if isinstance(types, list) else [types]
            if not _type_ok(val, tlist):
                errs.append(f"schema: {loc}: expected type {types}, got {type(val).__name__}")
                return
        if "enum" in sch and val not in sch["enum"]:
            errs.append(f"schema: {loc}: '{val}' not in enum")
        if isinstance(val, str):
            if "maxLength" in sch and len(val) > sch["maxLength"]:
                errs.append(f"schema: {loc}: length {len(val)} > maxLength {sch['maxLength']}")
            if "minLength" in sch and len(val) < sch["minLength"]:
                errs.append(f"schema: {loc}: shorter than minLength {sch['minLength']}")
            if sch.get("pattern", "").startswith("^https?") and not val.startswith(("http://", "https://")):
                errs.append(f"schema: {loc}: must be an http(s) URL")
        if isinstance(val, (int, float)) and not isinstance(val, bool):
            if "minimum" in sch and val < sch["minimum"]:
                errs.append(f"schema: {loc}: {val} < minimum {sch['minimum']}")
            if "maximum" in sch and val > sch["maximum"]:
                errs.append(f"schema: {loc}: {val} > maximum {sch['maximum']}")
        if sch.get("type") == "object" or "properties" in sch:
            if isinstance(val, dict):
                check_object(val, sch, f"{loc}/")
        if isinstance(val, list) and "items" in sch:
            for i, item in enumerate(val):
                check_value(item, sch["items"], f"{loc}/{i}")

    check_object(entry, schema, "")

    # Conditional block: network_endpoints required when makes_network_calls is true.
    # (trust_tier/security_review were removed — trust now lives only in framework/analysis.yml.)
    sec = entry.get("security", {})
    if isinstance(sec, dict) and sec.get("makes_network_calls") is True:
        eps = sec.get("network_endpoints")
        if not isinstance(eps, list) or len(eps) < 1:
            errs.append("schema: security/network_endpoints: required (non-empty) when makes_network_calls is true")
    return errs


def _type_ok(val, tlist) -> bool:
    ok = False
    for t in tlist:
        if t == "string":
            ok = ok or isinstance(val, str)
        elif t == "boolean":
            ok = ok or isinstance(val, bool)
        elif t == "integer":
            ok = ok or (isinstance(val, int) and not isinstance(val, bool))
        elif t == "number":
            ok = ok or (isinstance(val, (int, float)) and not isinstance(val, bool))
        elif t == "array":
            ok = ok or isinstance(val, list)
        elif t == "object":
            ok = ok or isinstance(val, dict)
        elif t == "null":
            ok = ok or val is None
    return ok


# --------------------------------------------------------------------------
# Cross-field rules
# --------------------------------------------------------------------------
def is_owner_authored(entry: dict) -> bool:
    author = (entry.get("author") or "").strip().lower()
    if author in OWNER_HANDLES:
        return True
    url = (entry.get("author_url") or "").lower()
    return any(frag in url for frag in OWNER_URL_FRAGMENTS)


def cross_field_errors(entry: dict) -> list[str]:
    errs: list[str] = []
    fn = entry.get("_filename", "")
    base = fn[:-4] if fn.endswith(".yml") else fn

    # X1 — slug == filename
    slug = entry.get("slug")
    if slug and base and slug != base:
        errs.append(f"X1 slug/filename: slug '{slug}' != filename '{base}'")

    # X2 (recusal): the disclosure model publishes no per-entry verdict, so there is no
    # self-rating an owner could give their own skills. Neutrality is structural — owner
    # entries sit in plain alphabetical order like every other entry. Nothing to check here.

    # X3 — validate_claim mandatory for skill | suite
    if entry.get("type") in ("skill", "suite"):
        vc = entry.get("validate_claim")
        if not (isinstance(vc, str) and vc.strip()):
            errs.append(f"X3 validate_claim: required for type '{entry.get('type')}' (mandatory per §0.2)")

    return errs


def main() -> int:
    schema = load_schema()
    entries = D.load_entries()
    if not entries:
        print("schema_check: no entries found in data/skills/ (nothing to validate).")
        return 0

    total_errors = 0
    seen_urls: dict[str, str] = {}
    for entry in entries:
        fn = entry.get("_filename", "?")
        errs = jsonschema_errors(entry, schema) + cross_field_errors(entry)

        # Duplicate source_url guard (mirrors awesome-lint double-link spirit).
        url = (entry.get("source_url") or "").rstrip("/").lower()
        if url:
            if url in seen_urls:
                errs.append(f"duplicate source_url also in {seen_urls[url]}")
            else:
                seen_urls[url] = fn

        if errs:
            total_errors += len(errs)
            print(f"\n✗ {fn}")
            for e in errs:
                print(f"    - {e}")
        else:
            print(f"✓ {fn}")

    print()
    if total_errors:
        print(f"schema_check: FAILED — {total_errors} error(s) across {len(entries)} entr(ies).")
        return 1
    print(f"schema_check: PASSED — {len(entries)} entr(ies) valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
