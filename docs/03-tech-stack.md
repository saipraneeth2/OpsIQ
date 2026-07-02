# 03 — Tech Stack

Every choice below is optimized for a solo founder with a CS background who has never shipped a product. Rules of thumb:

1. **Boring is beautiful.** No exotic frameworks. Use tools with enormous documentation and Stack Overflow presence.
2. **Free tiers first.** Every service listed has a free tier that covers the pilot.
3. **No vendor lock-in for anything expensive.** Cloud provider, database, LLM — all swappable.
4. **Multi-tenant from day one.** Data is scoped by `tenant_id` in every table, even if there's only one tenant.

---

## Backend

- **Python 3.11** — the founder knows Python; ML libraries live here anyway.
- **FastAPI** — modern, well-documented, async-ready, automatic OpenAPI docs.
- **Uvicorn** — ASGI server for FastAPI.
- **SQLAlchemy 2.0** (async) + **Alembic** — ORM and migrations.
- **APScheduler** (v1) → **Celery + Redis** (v2 when scale demands).
- **Pydantic v2** — request/response validation, config.

## Database

- **PostgreSQL 16** — managed on Railway (v1) or Supabase.
- **Redis** — for scheduled-task queue and caching (add when needed, not before).

## Computer vision

- **Ultralytics YOLOv8** — person detection + tracking. Open source, MIT-friendly commercial license only if used on-prem (verify current terms before selling).
- **OpenCV** — frame extraction, drawing, IoU tracker.
- **FFmpeg** — pull RTSP streams, chunk into files.
- **Torch** (CPU wheel for v1) — YOLO backend. Move to GPU only when store count > 10.

## Messaging

- **Telegram Bot API** — v1. Free, dead simple, works everywhere.
- **WhatsApp Business API** (via Meta or an aggregator like Gupshup / Kaleyra) — v2 when a paying customer demands it. WhatsApp is the actual home for Indian owners; Telegram is a starter shortcut.

## AI / LLM (v3 feature only)

- **Anthropic Claude API** — for the weekly insight summary. Sonnet is cheap enough for daily use at pilot scale.
- **OpenAI API** — fallback / A/B option.

## Hosting

- **Railway** or **Render** — for the FastAPI app (v1). $5–20/month.
- **Hetzner Cloud** (CX22, ~€5/mo) — better price/performance if you want to leave Railway.
- **Cloudflare** — DNS, TLS, later Cloudflare Tunnel for edge inference boxes at the store.
- **Vercel** — for the eventual Next.js dashboard (v2).

## Storage

- **Cloudflare R2** or **Backblaze B2** — for footage snippets we want to keep as evidence for anomalies. S3-compatible, zero egress fees.

## Dev tools

- **GitHub** — source, actions, project board.
- **GitHub Actions** — CI (lint, tests) from day one.
- **Ruff** — Python linter/formatter.
- **Pytest** — tests.
- **Docker** + **docker-compose** — reproducible local env; deploys to Railway.
- **direnv** or **dotenv** — env var management.

## Explicitly rejected (with reasons)

- **Kubernetes.** No. You are one person. Railway is fine.
- **A microservice architecture.** No. Monolith until it hurts. It won't hurt for years at this scale.
- **A custom-trained vision model.** No. YOLOv8 pretrained is state-of-the-art for person detection. Custom training is a distraction until we have thousands of hours of labeled footage.
- **Firebase / Firestore.** No. NoSQL for relational data will cost you a rewrite. Use Postgres.
- **A no-code platform.** No. You can code. No-code will hit a wall around F3 (reconciliation logic) and you'll rewrite anyway.

---

## Total monthly cost at pilot scale

| Service              | Cost (₹/mo) |
|----------------------|-------------|
| Cloud server         | 1,700       |
| Postgres (managed)   | 850         |
| Object storage       | 400         |
| Domain + Cloudflare  | 100         |
| Telegram             | 0           |
| Claude API (weekly)  | 850         |
| **Total**            | **~4,000**  |

At ₹50k budget, that's 12+ months of runway for the software layer alone.
