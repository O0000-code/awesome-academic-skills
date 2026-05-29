#!/usr/bin/env python3
"""Hard gate: every listed repo must be PUBLICLY reachable.

Why this exists: discovery/audit can run with an authenticated GitHub token, which
can see the maintainer's OWN private repos — so a private repo can slip into the list
(it happened once: o0000-code/deep-literature-search). A public index must contain only
public URLs, or every entry is a 404 for everyone else. This check fetches each entry's
repo URL **UNAUTHENTICATED** — exactly what an anonymous visitor sees — and fails (exit 1)
on anything that is not publicly HTTP 200.

It deliberately uses an anonymous request (no token, no `gh`); that is the whole point.

Usage:
  python scripts/check_public.py            # check all entries, exit 1 if any non-public
  python scripts/check_public.py --quiet     # only print failures
"""

from __future__ import annotations

import argparse
import concurrent.futures as _cf
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import data as D  # noqa: E402

_GH = re.compile(r"github\.com/([^/\s#?]+/[^/\s#?]+)")


def public_status(url: str) -> str:
    """Unauthenticated HTTP status for a repo URL. '200' = public; anything else
    (404 private/deleted, 451, etc.) = not publicly reachable. Non-GitHub hosts are
    checked by raw URL the same way."""
    m = _GH.search(url or "")
    target = f"https://github.com/{m.group(1)}" if m else (url or "")
    if not target:
        return "NO-URL"
    try:
        # -L follows the rename/redirect; no auth header is ever sent.
        r = subprocess.run(
            ["curl", "-s", "-o", os.devnull, "-w", "%{http_code}", "-L",
             "--max-time", "25", target],
            capture_output=True, text=True, timeout=30,
            env={**os.environ, "GITHUB_TOKEN": "", "GH_TOKEN": ""},  # strip any token
        )
        return r.stdout.strip() or "ERR"
    except Exception as e:  # noqa: BLE001
        return f"ERR:{type(e).__name__}"


def main() -> int:
    ap = argparse.ArgumentParser(description="Fail if any listed repo is not publicly reachable.")
    ap.add_argument("--quiet", action="store_true", help="only print non-public entries")
    args = ap.parse_args()

    entries = D.load_entries()
    bad = []
    with _cf.ThreadPoolExecutor(max_workers=16) as ex:
        futs = {ex.submit(public_status, e.get("source_url", "")): e for e in entries}
        for fut in _cf.as_completed(futs):
            e = futs[fut]
            code = fut.result()
            if code != "200":
                bad.append((e.get("slug", "?"), e.get("source_url", ""), code))

    if not args.quiet:
        D.eprint(f"check_public: {len(entries)} entries checked unauthenticated.")
    if bad:
        D.eprint(f"check_public: FAILED — {len(bad)} repo(s) NOT publicly reachable:")
        for slug, url, code in sorted(bad):
            D.eprint(f"  [{code}] {slug} -> {url}")
        D.eprint("A public index must contain only public repos. Remove or fix these "
                 "(a private repo seen via an authenticated token must NOT be listed).")
        return 1
    if not args.quiet:
        D.eprint("check_public: PASSED — all repos are publicly reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
