# 01 — MVP Spec

## Definition of MVP

The MVP is complete when, for 30 consecutive days, the owner receives a **daily automated 9pm message** across all three pilot stores containing:

1. Yesterday's verified sales (from POS).
2. Yesterday's walk-in count (from CCTV computer vision).
3. Conversion rate: bills ÷ walk-ins.
4. Per-staff performance ranking for the day.
5. Any flagged anomalies (unbilled visits, cash mismatch, no-show staff).

Nothing else. No dashboard, no mobile app, no AI-generated insights. If the owner reads this message every day for 30 days and acts on it at least three times, the MVP has succeeded.

## In scope (v1)

### F1 — Walk-in counting
- Pull footage from the store's existing CCTV (RTSP or vendor cloud API).
- Run YOLOv8 person detection on the entry-camera stream.
- Deduplicate people across frames using a simple IoU tracker.
- Emit hourly and daily walk-in counts.

### F2 — POS sales ingestion
- **Salon (Cheap and Best):** salon uses a POS; ingest via CSV export (manual daily upload → automated when possible).
- **Lenskart stores:** franchisee portal provides daily sales; scrape or CSV-export nightly.
- Store rows per bill: time, item, amount, staff who closed the sale.

### F3 — Reconciliation
- Match walk-ins to bills within a rolling time window.
- Flag: bills > walk-ins (data error?), walk-ins ≫ bills (unbilled visits?), cash short by > ₹200 at day close.

### F4 — Staff performance
- **Salon:** stylist signs in on a tablet before each customer (30-second tap flow). Attributes revenue + service duration to the correct stylist.
- **Lenskart:** POS already attributes bills to the salesperson.
- Weekly per-staff score: (revenue × conversion rate) normalized against store average.

### F5 — Daily report delivery
- Telegram bot (v1, free) sends structured message at 9pm.
- Owner can reply `/details <store>` to get a per-store breakdown.
- Message format is designed for phone-glance readability, not desktop dashboards.

## Explicitly out of scope (v1)

- Web dashboard or mobile app.
- Face recognition of staff or customers.
- Real-time alerts (all v1 reports are next-day).
- AI-generated recommendations (v3).
- Inventory tracking.
- Customer loyalty / CRM.
- Payroll / HR features.
- Multi-tenant admin UI (the code is multi-tenant-ready, but there's no self-serve signup).

## Success metrics — how we know it worked

At end of the 30-day continuous run, we should be able to say YES to at least 4 of these 6:

- Reports delivered on time for ≥ 27 of 30 days (90% reliability).
- Walk-in counts within ±10% of manually verified spot-checks.
- Owner reports at least 3 concrete actions taken based on the report (e.g., "spoke to Suresh about low conversion", "found Tuesday cash short").
- At least one previously-hidden anomaly surfaced (unbilled cash, no-show staff, sales-drop pattern).
- Owner voluntarily forwards the report to a business partner or another operator at least once.
- Owner says "I would pay for this" (with a specific ₹ amount) when asked directly.

If fewer than 4 are YES, we iterate on the report content and delivery — not on adding features.

## What v2 looks like (after MVP validates)

- Automated POS pulling (no manual CSVs).
- End-of-week owner summary with LLM-generated insights.
- Second customer onboarded (someone from dad's network).
- Basic web dashboard for historical trends.
- Configurable anomaly thresholds per store.
