# 00 — Vision

## Why this exists

Every multi-location business owner runs into the same wall: they cannot personally be in every store, so they hire General Managers to be their eyes and ears. But GMs are expensive (₹50k–₹1L per month in India), they filter information before it reaches the owner, and they have their own incentive misalignments — a GM who reports "everything's fine" every day is not necessarily telling the truth.

What if the owner could get an *unfiltered* daily view of every store — verified sales, staff attendance, customer flow, cash discrepancies — without a human middleman?

Two things make this possible in 2026 that were not possible five years ago:

1. **CCTV is already installed almost everywhere.** Even small tier-2 town stores in India have IP cameras with cloud connectivity. The hardware is a sunk cost.
2. **Computer vision has commoditized.** YOLOv8 runs on a ₹15,000 mini-PC. Person counting, pose detection, and object tracking are open-source and reliable.

The only missing layer is the **software that turns these inputs into a trustworthy daily report the owner actually reads.** That's OpsIq.

## The core insight

The right framing is **not** "replace the General Manager." Good GMs handle nuance — staff conflicts, supplier disputes, angry customers, local marketing — that software cannot. The right framing is:

> **OpsIq is a co-pilot that lets one owner (or one GM) effectively oversee 10 locations instead of 3.**

We do the boring 70% of the GM's job automatically: the daily reporting, the reconciliation, the anomaly flagging, the performance ranking. We leave the messy 30% to humans, where they add real value.

## What we are betting on

1. **Owners will trust software-generated numbers more than manager-reported numbers**, once the software proves reliable for 60 days.
2. **The unit economics work at ₹15–25k per store per month** — less than half a GM's salary, so switching from "one GM per 3 stores" to "OpsIq + one GM per 10 stores" saves the owner money immediately.
3. **The Indian tier-2 franchise market is underserved.** Existing tools (Wobot, Verkada, etc.) target enterprise or QSR. Independent multi-location owners with 3–20 stores have no purpose-built tool.

## What we are explicitly NOT building (yet)

- **Full GM replacement.** Human judgment stays.
- **A "beautiful analytics dashboard."** Owners in this segment don't log in to dashboards; they read WhatsApp messages. Ship where the user actually is.
- **AI-powered profit-maximization suggestions in v1.** They sound impressive and are worthless without verified underlying data. This is a v3 feature after 60 days of clean data collection.
- **Face recognition of employees.** Legal minefield under India's DPDP Act and morale-destroying. Use tablet sign-in for staff identity instead.
- **A hardware business.** We do not sell cameras. We work with what the store already has.

## The founder's edge

The founding team has direct operator access to three pilot stores across two Indian franchise/independent business types. This means:

- Free, high-signal design partners for the entire first year.
- Realistic constraints (tier-2 town wifi, mixed-tech staff, cash-heavy environment) baked into the product from day one.
- A first case study to sell to the next 10 customers, drawn from the founder's family network of franchise operators.
