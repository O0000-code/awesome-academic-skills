#!/usr/bin/env python3
"""Flag entries whose repos look unmaintained (RF §4 check #7, selfhosted's
check-unmaintained-projects). Reads the CI-maintained `updated_at` / `archived`
fields (refreshed by update_metadata.py) and reports entries with no activity in
6-12 months or that are archived.

This NEVER auto-delists (C7/R-RF-4: scheduled failures are labels for review,
not auto-removals). It emits a markdown report; check-unmaintained.yml turns that
into / updates a tracking issue for a human to triage.

Usage:
  python scripts/check_unmaintained.py                 # print report to stdout
  python scripts/check_unmaintained.py --months 9       # custom stale threshold
  python scripts/check_unmaintained.py --out report.md  # also write to a file
"""

from __future__ import annotations

import argparse
import datetime as _dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import data as D  # noqa: E402


def months_since(date_str: str | None, today: _dt.date) -> float | None:
    if not date_str:
        return None
    try:
        d = _dt.date.fromisoformat(date_str[:10])
    except ValueError:
        return None
    return (today - d).days / 30.44


def main() -> int:
    ap = argparse.ArgumentParser(description="Flag stale / archived entries (no auto-delist).")
    ap.add_argument("--months", type=float, default=9.0,
                    help="Stale threshold in months (default 9; RF window is 6-12).")
    ap.add_argument("--out", help="Also write the report to this path.")
    args = ap.parse_args()

    today = _dt.date.today()
    entries = D.load_entries()

    archived = []
    stale = []
    unknown = []
    for e in entries:
        slug = e.get("slug")
        name = e.get("name", slug)
        url = e.get("source_url", "")
        if e.get("archived"):
            archived.append((name, url, "archived"))
            continue
        m = months_since(e.get("updated_at"), today)
        if m is None:
            unknown.append((name, url, "no updated_at on record"))
        elif m >= args.months:
            stale.append((name, url, f"{m:.1f} months since last push"))

    lines = []
    lines.append("## Unmaintained-entry sweep")
    lines.append("")
    lines.append(f"_As of {today.isoformat()}; stale threshold = {args.months} months. "
                 "This is a review aid — entries are NOT auto-removed (R-RF-4)._")
    lines.append("")

    def section(title, rows):
        lines.append(f"### {title} ({len(rows)})")
        if not rows:
            lines.append("- none")
        else:
            for name, url, why in rows:
                lines.append(f"- [{name}]({url}) — {why}")
        lines.append("")

    section("Archived upstream", archived)
    section("Possibly stale", stale)
    section("Unknown activity (needs a metadata refresh)", unknown)

    report = "\n".join(lines)
    print(report)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(report + "\n")

    flagged = len(archived) + len(stale)
    D.eprint(f"\ncheck_unmaintained: {flagged} flagged ({len(archived)} archived, "
             f"{len(stale)} stale), {len(unknown)} unknown, {len(entries)} total.")
    # Informational only — exit 0 regardless (no auto-delist).
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
