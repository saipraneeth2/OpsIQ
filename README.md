# OpsIq

**A multi-store operations platform for franchise and multi-location owners.**

OpsIq gives owners of multi-location businesses a single, trustworthy daily view of what's actually happening in each of their stores — verified sales, staff performance, and customer-flow insights — without depending on a General Manager to filter and report the truth.

---

## The problem

Multi-location owners (franchise operators, retail chains, salon groups, restaurant owners) rely on General Managers to tell them what's happening across their stores. This model has three chronic failures:

1. **The numbers can't be trusted.** The GM reports what the store manager tells them, who reports what the counter staff writes down. By the time it reaches the owner, cash leakage, unbilled sales, and inflated staffing hours have all crept in.
2. **Problems surface late.** A sales dip that starts on a Monday is only noticed at the end-of-month review, three weeks after the customer behavior changed.
3. **The weakest performer stays invisible.** Owners intuit who their strong and weak staff are, but rarely have per-person data to act on it.

## The product

OpsIq is a lightweight software layer that sits on top of the store's **existing** CCTV cameras and POS system. It:

- Counts customer walk-ins from CCTV using computer vision.
- Pulls sales data from the POS.
- Cross-checks the two, plus the end-of-day cash count, to surface unbilled visits and cash discrepancies.
- Ranks staff by conversion, engagement time, and revenue per shift.
- Sends the owner a daily 9pm WhatsApp/Telegram summary — no dashboard to open, no manager to ask.
- (Later) Uses AI to summarize weekly trends and suggest concrete actions.

## Who it's for

- Franchise owners running 3–20 locations.
- Multi-store retail (opticals, mobile stores, salons, QSR, kirana, pharmacies).
- Single-store owners who work remotely from their business.

## Repo layout

```
opsiq/
├── docs/                  # The plan — read these first
│   ├── 00-vision.md
│   ├── 01-mvp-spec.md
│   ├── 02-roadmap-90-days.md
│   ├── 03-tech-stack.md
│   ├── 04-architecture.md
│   ├── 05-pilot-stores.md
│   └── 06-week-1-checklist.md
├── backend/               # FastAPI service — API, database, scheduled jobs
├── vision/                # YOLO-based walk-in counting and staff activity detection
├── bot/                   # Telegram/WhatsApp bot that delivers the daily report
├── scripts/               # One-off scripts, POS pullers, orchestration
├── .env.example           # Environment variables template (NEVER commit real .env)
└── .gitignore
```

## Start here

1. Read [`docs/00-vision.md`](docs/00-vision.md) — the product thesis.
2. Read [`docs/02-roadmap-90-days.md`](docs/02-roadmap-90-days.md) — the actual build plan.
3. Read [`docs/06-week-1-checklist.md`](docs/06-week-1-checklist.md) — what to do this week.

## Status

Pre-alpha. No code yet. Pilot planned across 3 stores in Andhra Pradesh, India (one salon, two optical retail franchises) beginning June 2026.

## Tech stack (planned)

Python 3.11 · FastAPI · PostgreSQL · Ultralytics YOLOv8 · Telegram Bot API · Anthropic Claude API · Deployed on Railway/Hetzner.

## License

Proprietary — all rights reserved. See [LICENSE](LICENSE).
