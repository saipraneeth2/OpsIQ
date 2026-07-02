"""Manual daily report generator — Month 1 glue.

Run this every night in Month 1 (before the backend exists). It stitches
together the walk-in count, a CSV of POS bills, and prints a report
suitable for copy-paste into WhatsApp/Telegram.

Usage:
    python scripts/daily_report.py \\
        --store "Cheap and Best" \\
        --video ./data/2026-05-20-entry.mp4 \\
        --pos-csv ./data/2026-05-20-sales.csv \\
        --date 2026-05-20
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass


@dataclass
class DailyStats:
    store: str
    date: str
    walkins: int
    bill_count: int
    total_sales: float

    @property
    def conversion_pct(self) -> float:
        return (self.bill_count / self.walkins * 100) if self.walkins else 0.0

    @property
    def unbilled_visits(self) -> int:
        return max(self.walkins - self.bill_count, 0)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a daily WhatsApp-ready report.")
    p.add_argument("--store", required=True)
    p.add_argument("--video", required=True, help="Entry-camera video for the day.")
    p.add_argument("--pos-csv", required=True, help="CSV: bill_id,ts,amount,staff.")
    p.add_argument("--date", required=True)
    return p.parse_args()


def count_walkins_placeholder(video_path: str) -> int:
    # Replace with a real call to vision/count_walkins.py in Week 2.
    print(f"[scripts.daily_report] (placeholder) counting walk-ins in {video_path}")
    return 0


def read_pos_csv(path: str) -> tuple[int, float]:
    total = 0.0
    count = 0
    with open(path, newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            count += 1
            total += float(row.get("amount", 0) or 0)
    return count, total


def render_report(stats: DailyStats) -> str:
    lines = [
        f"*OpsIq daily — {stats.store} — {stats.date}*",
        "",
        f"Walk-ins: *{stats.walkins}*",
        f"Bills: *{stats.bill_count}*",
        f"Sales: *₹{stats.total_sales:,.0f}*",
        f"Conversion: *{stats.conversion_pct:.0f}%*",
    ]
    if stats.unbilled_visits > 0:
        lines.append(f"⚠ Possible unbilled visits: *{stats.unbilled_visits}*")
    return "\n".join(lines)


def main() -> None:
    args = parse_args()
    walkins = count_walkins_placeholder(args.video)
    bill_count, total_sales = read_pos_csv(args.pos_csv)
    stats = DailyStats(
        store=args.store,
        date=args.date,
        walkins=walkins,
        bill_count=bill_count,
        total_sales=total_sales,
    )
    print(render_report(stats))


if __name__ == "__main__":
    main()
