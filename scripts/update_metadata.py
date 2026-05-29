#!/usr/bin/env python3
"""Fill the CI-maintained fields of each data/skills/*.yml from the GitHub API.

Author-supplied fields are never touched. This updates only:
  stargazers_count, updated_at, archived, current_release{tag,published_at}.

Mirrors awesome-selfhosted's daily-update-metadata job (RF §1.2). Run on a
schedule (update-metadata.yml). Uses GITHUB_TOKEN if present (higher rate limit);
falls back to unauthenticated requests (60/hr) otherwise. Re-emits each YAML
with author fields preserved and ordering stable.

Usage:
  GITHUB_TOKEN=... python scripts/update_metadata.py            # update all
  python scripts/update_metadata.py --dry-run                    # show, don't write
  python scripts/update_metadata.py --only <slug>                # one entry
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import data as D  # noqa: E402

import yaml  # noqa: E402

API = "https://api.github.com"


def gh_get(path: str) -> dict | None:
    url = f"{API}{path}"
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "awesome-academic-skills-metadata")
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        D.eprint(f"  GitHub API {e.code} for {path}")
        return None
    except (urllib.error.URLError, TimeoutError) as e:
        D.eprint(f"  network error for {path}: {e}")
        return None


def parse_owner_repo(source_url: str) -> tuple[str, str] | None:
    m = re.match(r"https?://github\.com/([^/]+)/([^/#?]+)", source_url.strip())
    if not m:
        return None
    owner, repo = m.group(1), m.group(2)
    repo = repo.removesuffix(".git")
    return owner, repo


def fetch_metadata(owner: str, repo: str) -> dict | None:
    data = gh_get(f"/repos/{owner}/{repo}")
    if not data:
        return None
    meta = {
        "stargazers_count": data.get("stargazers_count"),
        "updated_at": (data.get("pushed_at") or "")[:10] or None,
        "archived": bool(data.get("archived", False)),
        "current_release": {"tag": None, "published_at": None},
    }
    rel = gh_get(f"/repos/{owner}/{repo}/releases/latest")
    if rel:
        meta["current_release"] = {
            "tag": rel.get("tag_name"),
            "published_at": (rel.get("published_at") or "")[:10] or None,
        }
    return meta


def update_entry_file(path: str, meta: dict, dry_run: bool) -> bool:
    """Rewrite only the CI-maintained keys, preserving everything else.

    We load → patch the keys → dump. Comments are not preserved by PyYAML; the
    CI-maintained block lives at the end of each file and is machine-owned, so
    this is acceptable (and matches selfhosted's generator-owned-tail model).
    """
    with open(path, "r", encoding="utf-8") as fh:
        doc = yaml.safe_load(fh)
    changed = False
    for key in ("stargazers_count", "updated_at", "archived", "current_release"):
        if doc.get(key) != meta[key]:
            doc[key] = meta[key]
            changed = True
    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as fh:
            yaml.safe_dump(doc, fh, sort_keys=False, allow_unicode=True, default_flow_style=False)
    return changed


def main() -> int:
    ap = argparse.ArgumentParser(description="Refresh CI-maintained metadata from GitHub.")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="Only update the entry with this slug.")
    args = ap.parse_args()

    entries = D.load_entries()
    if args.only:
        entries = [e for e in entries if e.get("slug") == args.only]
        if not entries:
            D.eprint(f"no entry with slug {args.only!r}")
            return 1

    if not os.environ.get("GITHUB_TOKEN"):
        D.eprint("note: GITHUB_TOKEN not set — using unauthenticated API (60 req/hr).")

    updated = 0
    failed = 0
    for e in entries:
        slug = e.get("slug")
        pr = parse_owner_repo(e.get("source_url", ""))
        if not pr:
            D.eprint(f"  {slug}: source_url is not a github.com repo — skipped")
            continue
        owner, repo = pr
        meta = fetch_metadata(owner, repo)
        if not meta:
            failed += 1
            print(f"  {slug}: metadata fetch failed (repo missing or rate-limited)")
            continue
        changed = update_entry_file(e["_path"], meta, args.dry_run)
        flag = "updated" if changed else "unchanged"
        if changed:
            updated += 1
        print(f"  {slug}: {flag} — ★{meta['stargazers_count']} pushed {meta['updated_at']} "
              f"release {meta['current_release']['tag']}")

    print(f"\nupdate_metadata: {updated} updated, {failed} failed, {len(entries)} total"
          + (" (dry-run)" if args.dry_run else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
