# 05 — Pilot Stores

Three pilot locations across two verticals in Andhra Pradesh, India.

## Store A — Cheap and Best (salon)

| Attribute        | Value                                    |
|------------------|------------------------------------------|
| Vertical         | Hair salon (independent)                 |
| Ownership        | Family-owned, full operational control   |
| POS              | Yes (brand TBD in week 1 discovery)      |
| CCTV             | ~6 cameras, cloud-connected              |
| Wifi             | Stable                                   |
| Franchisor rules | None (independent business)              |
| Primary KPI      | Walk-ins vs bills, stylist conversion    |

**Why this is the ideal first pilot:** no franchisor to negotiate with, full data access, cash-heavy so anomalies are common and useful, short customer cycle (30–90 min per service) so feedback loops are fast.

**Specific hypotheses to test here:**
- Walk-in count from CCTV correlates within ±10% of manual counts.
- Comparing walk-ins to bills surfaces at least one unbilled visit per week.
- Per-stylist revenue ranking is stable enough over 30 days to be actionable.

## Store B — Lenskart franchise, Bhimavaram

| Attribute        | Value                                    |
|------------------|------------------------------------------|
| Vertical         | Optical retail (franchise)               |
| Ownership        | Family-owned, franchise of Lenskart      |
| POS              | Provided by Lenskart HQ                  |
| CCTV             | ~6 cameras, cloud-connected              |
| Wifi             | Stable                                   |
| Franchisor rules | **Verify before adding vision analytics.** Lenskart may have restrictions on third-party software touching store data or video. Non-blocking for owner-side reporting on top of publicly-available (to the franchisee) data. |
| Primary KPI      | Walk-ins → greet time → conversion       |

**Why this pilot matters:** Lenskart HQ already gives the owner sales data through their franchisee app. Our value-add is the *pre-sale funnel* — footfall, greet time, engagement — which HQ does not see. This is where the "co-pilot" thesis is tested.

**Specific hypotheses:**
- Conversion (bills ÷ walk-ins) will vary meaningfully between Bhimavaram and Kakinada, and the difference will be explainable by staff behavior visible on camera.
- Greet time (walk-in → staff approach) will predict conversion.

## Store C — Lenskart franchise, Kakinada

Same setup as Bhimavaram. Run in parallel from month 2 to create a direct like-for-like comparison. Same product, same brand SOPs — any operational difference is signal.

---

## Pilot governance

- **Consent notices** posted in each store (required by India's DPDP Act). Template in `docs/legal/` (to be added).
- **Staff briefing** before any camera analytics run in production. Frame as "customer flow analytics" — honest, non-punitive.
- **No footage leaves the country in v1.** Cloud server region: `ap-south-1` (Mumbai) or Hetzner Helsinki as a compromise.
- **Owner is the only recipient** of every report in v1. No dashboards, no shared portals.

## What we're NOT doing in the pilot

- Not sharing data or vision analytics with Lenskart HQ (the franchisor). This is purely the franchisee's own data.
- Not identifying individual customers (no face recognition, no re-ID).
- Not identifying staff by face. Salon staff sign in on a tablet; Lenskart staff are identified via POS-attributed sales.
- Not making staffing/firing decisions based on OpsIq data during the pilot. Data collection only, decisions still human.
