# 02 — 90-Day Roadmap

The plan is deliberately conservative. Every milestone assumes nights-and-weekends effort (10–15 hrs/week) alongside a day job. If more hours are available, timelines compress; if fewer, they stretch.

---

## Month 1 — Wire up the data (May 15 → June 15)

**Goal:** By the end of month 1, the owner receives a **manually-generated** WhatsApp report every night at 9pm containing sales, walk-ins, and staff activity for one pilot store (Cheap and Best salon).

### Week 1 (May 15–22): Discovery
- Confirm CCTV vendor + how to pull footage (RTSP URL, cloud API, or physical NVR access).
- Get salon POS export sample (CSV or screenshot).
- Get Lenskart franchisee-portal login and confirm daily sales format.
- Provision cloud server (Hetzner CX22 or Railway).
- Set up GitHub repo (this one), CI-lite, project board.

### Week 2 (May 23–29): First walk-in count
- Download one day of entry-camera footage from the salon.
- Run YOLOv8 on it locally, count unique person entries.
- Compare against manual count. Target: within 15% accuracy.

### Week 3 (May 30 – June 5): Manual daily report
- Every day, download previous day's footage, run counter, pull POS sales, type a WhatsApp message to the owner by 9pm.
- Get feedback. Does the owner read it? What does he look at first? What does he ignore?

### Week 4 (June 6–15): Learn and adjust
- Log which numbers actually matter to the owner.
- Redesign the report based on 2 weeks of feedback.
- Draft the automation spec for month 2.

**Deliverable:** A manual daily-report workflow that the owner values enough to read every day.

---

## Month 2 — Automate (June 15 → July 15)

**Goal:** The Cheap and Best daily report is fully automated. Lenskart Bhimavaram is added.

### Week 5–6: Backend
- FastAPI service on the cloud server.
- PostgreSQL schema: stores, cameras, sales, walkins, staff, reports.
- Scheduled worker (APScheduler or Celery beat) that runs the pipeline nightly.

### Week 7: Vision pipeline
- Automated pull of footage (RTSP recording or cloud API).
- Overnight batch YOLO run.
- Store walk-in counts in DB.

### Week 8: Bot + POS + staff
- Telegram bot posting the auto-generated report at 9pm.
- Salon POS ingestion automated.
- Tablet sign-in flow for stylists (a stupid-simple web page — no login, just tap stylist name → tap "Start service" → tap "End service" → tap "Bill").
- Add Lenskart Bhimavaram (POS via franchisee portal scraping, walk-ins from CCTV).

**Deliverable:** Two stores running fully automated for at least 7 consecutive days by end of month.

---

## Month 3 — Harden and decide (July 15 → August 15)

**Goal:** All three stores running for 30 continuous days without manual intervention. Decision made on next 90 days.

### Week 9–10: Reliability
- Add Lenskart Kakinada.
- Monitoring: alert if any store's pipeline fails to run.
- Handle: camera offline, POS export missing, wifi outage, bot API rate limits.
- Fix every bug the owner encounters within 48 hours.

### Week 11: First AI insight
- End-of-week LLM summary via Claude API: 3 bullet points on trends across all 3 stores.
- Optional: `/insights` command in Telegram bot.

### Week 12: Validate and decide
- 30-day retrospective with the owner. Score against the 6 success metrics in [`01-mvp-spec.md`](01-mvp-spec.md).
- If ≥ 4 YES: begin second customer search.
- If < 4 YES: iterate on the report, do NOT add features.

**Deliverable:** Written decision memo — go, no-go, or pivot.

---

## After day 90 (post-MVP)

Two possible paths, chosen based on data from month 3, not before:

**Path A — Bootstrap SaaS.** Onboard 10 paying customers from the founder's network at ₹15–25k/mo per store. Build a self-serve onboarding flow. Stay solo or hire one part-timer. Aim for ₹5–10L MRR by end of year 1.

**Path B — Venture-backed.** If growth signals are strong and there's appetite to build a platform (multiple verticals, self-serve, integrations), start a pre-seed raise. Requires a cofounder — do not do this alone.

Neither path is chosen before month 3. Data first.
