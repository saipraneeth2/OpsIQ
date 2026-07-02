# 04 — Architecture

## High-level flow

```
┌────────────────────────────────────────────────────────────────────┐
│                          Each Pilot Store                          │
│                                                                    │
│   ┌──────────────┐    ┌──────────────┐    ┌────────────────────┐   │
│   │ CCTV cameras │    │  Store POS   │    │ Stylist sign-in    │   │
│   │ (cloud/RTSP) │    │  (Lenskart / │    │ tablet (salon only)│   │
│   │              │    │  salon POS)  │    │                    │   │
│   └──────┬───────┘    └──────┬───────┘    └─────────┬──────────┘   │
│          │                   │                      │              │
└──────────┼───────────────────┼──────────────────────┼──────────────┘
           │                   │                      │
           │ RTSP / cloud API  │ CSV export / scrape  │ HTTPS
           │                   │                      │
           ▼                   ▼                      ▼
┌────────────────────────────────────────────────────────────────────┐
│                     OpsIq Cloud (Railway / Hetzner)                │
│                                                                    │
│   ┌────────────────┐    ┌────────────────┐    ┌────────────────┐   │
│   │  Vision Worker │    │  POS Worker    │    │  API (FastAPI) │   │
│   │  (YOLOv8)      │    │  (nightly)     │    │                │   │
│   └────────┬───────┘    └────────┬───────┘    └────────┬───────┘   │
│            │                     │                     │           │
│            └──────────┬──────────┴─────────────────────┘           │
│                       ▼                                            │
│              ┌────────────────┐                                    │
│              │   PostgreSQL   │                                    │
│              └────────┬───────┘                                    │
│                       │                                            │
│                       ▼                                            │
│              ┌────────────────┐    ┌───────────────────────────┐   │
│              │ Report Builder │───▶│ Telegram Bot (delivers    │   │
│              │ (9pm cron)     │    │ daily message to owner)   │   │
│              └────────────────┘    └───────────────────────────┘   │
└────────────────────────────────────────────────────────────────────┘
```

## Components

### Vision Worker
Runs nightly. For each configured camera:
1. Pull yesterday's footage (RTSP-recorded segments or cloud API download).
2. Run YOLOv8 on entry-camera frames at 2 fps.
3. Track detections across frames (simple IoU tracker → later ByteTrack).
4. Emit unique-entry count per hour.
5. Write to `walkins` table.

### POS Worker
Runs nightly. For each store:
- **Salon:** ingest yesterday's POS CSV export (v1: manual upload, v2: API/scrape).
- **Lenskart:** headless-browser scrape of the franchisee portal, dump into DB.
- Normalize into a common `sales` table with `bill_id, timestamp, amount, staff_id, items`.

### Staff sign-in service
Salon only (v1). A dead-simple public web page hosted at `salon.opsiq.in`:
- Grid of stylist names.
- Tap name → tap "Start service" → tap "End" → tap "Bill".
- Writes to `staff_activity` table.
- No auth (kiosk is trusted local device). PIN-protect if abuse becomes an issue.

### Report Builder
Cron job at 9pm IST. For each tenant:
1. Query yesterday's `walkins`, `sales`, `staff_activity`.
2. Compute: total sales, walk-ins, conversion %, per-staff score, anomalies.
3. Render as a structured message (Markdown for Telegram).
4. Enqueue for delivery.

### Bot / delivery layer
- Telegram Bot: sends the rendered message to the owner's chat.
- Owner can `/details <store>`, `/staff`, `/anomalies` for follow-ups.
- v2: WhatsApp Business channel with the same interface.

## Data model (v1 sketch)

```
tenants          (id, name, created_at)
stores           (id, tenant_id, name, city, timezone)
cameras          (id, store_id, label, rtsp_url_or_key, entry_camera bool)
staff            (id, store_id, name, active)
walkins          (id, store_id, ts_hour, count, source_camera_id)
sales            (id, store_id, bill_id, ts, amount, staff_id, items_json)
staff_activity   (id, staff_id, ts_start, ts_end, service_type)
reports          (id, tenant_id, store_id, date, payload_json, delivered_at)
anomalies        (id, store_id, date, kind, details_json, resolved bool)
```

Every table is scoped by `tenant_id` (directly or transitively via `store_id`). All queries are filtered on `tenant_id` at the ORM layer.

## Where the AI actually lives

Two places, and only these two:

1. **YOLOv8** for person detection. Local inference, no external API calls.
2. **Claude API** for weekly natural-language summary (v3). Prompt with the last week's rows, get 3 bullet points back.

Everything else is deterministic SQL / Python.

## What's NOT here

- No microservices. One FastAPI app, one worker process, one DB.
- No real-time streaming. All batch, all nightly.
- No message queue in v1 (APScheduler suffices). Redis + Celery when needed.
- No customer-facing dashboard. The Telegram message *is* the UI.
- No user auth on OpsIq itself in v1. The bot chat is the auth boundary.
