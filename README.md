# OpsIq

**Pre-alpha. Planning documents and code scaffolding only.**

OpsIq is an operations platform in development for multi-store owners, designed to reconcile POS sales against end-of-day cash, flag unbilled sales and cash discrepancies, and send the owner a nightly KPI summary.

---

## The problem

Multi-location owners (franchise operators, retail chains, salon groups, restaurant owners) rely on General Managers to tell them what's happening across their stores. This model has three chronic failures:

1. **The numbers can't be trusted.** The GM reports what the store manager tells them, who reports what the counter staff writes down. By the time it reaches the owner, cash leakage, unbilled sales, and inflated staffing hours have all crept in.
2. **Problems surface late.** A sales dip that starts on a Monday is only noticed at the end-of-month review, three weeks after the customer behavior changed.
3. **The weakest performer stays invisible.** Owners intuit who their strong and weak staff are, but rarely have per-person data to act on it.

## Core design (first version)

- Pull sales data from the store's existing POS.
- Reconcile POS sales against the end-of-day cash count.
- Flag unbilled sales and cash discrepancies.
- Send the owner a nightly KPI summary.

## Planned later

These ideas are on the roadmap, not built:

- Count customer walk-ins from existing CCTV cameras with computer vision, and cross-check them against POS sales.
- Per-staff performance views (conversion and revenue per shift).
- Deliver the nightly summary through WhatsApp or Telegram.
- AI-written weekly trend summaries with suggested actions.

## Who it's for

- Franchise owners running 3 to 20 locations.
- Multi-store retail (opticals, mobile stores, salons, QSR, kirana, pharmacies).
- Single-store owners who work remotely from their business.

## Repo layout

```
opsiq/
├── docs/                  # The plan: read these first
│   ├── 00-vision.md
│   ├── 01-mvp-spec.md
│   ├── 02-roadmap-90-days.md
│   ├── 03-tech-stack.md
│   ├── 04-architecture.md
│   ├── 05-pilot-stores.md
│   └── 06-week-1-checklist.md
├── backend/               # FastAPI service scaffold: API, database, scheduled jobs
├── vision/                # Walk-in counting scaffold (planned later)
├── bot/                   # Messaging bot scaffold for the nightly summary
├── scripts/               # One-off scripts, POS pullers, orchestration
├── .env.example           # Environment variables template (never commit a real .env)
└── .gitignore
```

## Start here

1. Read [`docs/00-vision.md`](docs/00-vision.md) for the product thesis.
2. Read [`docs/02-roadmap-90-days.md`](docs/02-roadmap-90-days.md) for the build plan.
3. Read [`docs/06-week-1-checklist.md`](docs/06-week-1-checklist.md) for the first steps.

## Tech stack (planned)

Python 3.11 · FastAPI · PostgreSQL · Telegram Bot API · Anthropic Claude API. Computer vision (Ultralytics YOLOv8) comes later.

## License

Proprietary, all rights reserved. See [LICENSE](LICENSE).
