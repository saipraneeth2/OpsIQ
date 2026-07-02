# scripts/

One-off and utility scripts. This is the "sharp knives" folder — nothing here is production-grade, but a lot of it saves the day.

## Contents (planned)

- `daily_report.py` — the Month-1 manual glue script: pulls yesterday's footage, runs the walk-in counter, reads a CSV of POS sales, prints a report you can copy-paste into WhatsApp.
- `lenskart_scrape.py` (Month 2) — headless-browser script to pull daily sales from the Lenskart franchisee portal.
- `backfill_walkins.py` — run the vision pipeline against archived footage for historical baselines.

## Convention

Every script here should:
1. Be runnable standalone (`python scripts/foo.py`).
2. Print help with `--help`.
3. Never touch the production database directly without a `--tenant-id` flag and a confirmation prompt.
4. Log to stdout, not to a file.
