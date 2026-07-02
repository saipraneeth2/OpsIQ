# 06 — Week 1 Checklist

Do these things before writing any real code. Timebox: 7 days.

## Discovery (with dad + local tech person)

- [ ] CCTV brand and model at each store. (Hikvision? CP Plus? Dahua? Something else?)
- [ ] Which app or website does dad use to view the footage? Log in and take screenshots.
- [ ] Admin credentials for the CCTV cloud (create a separate admin user for OpsIq — do not use dad's personal login).
- [ ] Can you get an RTSP URL from the camera or the NVR? Ask the tech person.
- [ ] What POS does Cheap and Best use? Brand, version. Can it export CSV?
- [ ] Log into Lenskart franchisee portal. Find where per-day, per-store sales appear. Screenshot the flow.
- [ ] How does Lenskart POS attribute a sale to a salesperson? (Every bill has a staff ID — confirm.)
- [ ] Wifi speed test at each store (SpeedTest.net or fast.com from dad's phone in-store). Record down/up Mbps.

## Personal setup (in the US)

- [ ] Fresh Python 3.11 + poetry or uv installed.
- [ ] Clone this repo locally.
- [ ] Create a Telegram account if you don't have one, then create a bot via @BotFather. Save the bot token securely.
- [ ] Send yourself a "Hello" message via the bot using a 20-line Python script. This is the single most important smoke test — if this works, delivery is solved forever.
- [ ] Create a Railway account (free tier). Don't provision anything yet.
- [ ] Create an Anthropic API key for later. Don't use it yet.

## Legal + privacy (do NOT skip)

- [ ] Draft a one-page consent notice in English + Telugu, to be posted at the entrance of each store. Language: "This store uses CCTV analytics for operational purposes. No individual customer or staff data is stored. For questions contact [owner phone]."
- [ ] Verify the Lenskart franchise agreement doesn't prohibit third-party analytics on store data. If it does, either negotiate or exclude Lenskart stores from vision analytics (keep them for POS reconciliation only).

## Honest commitments

- [ ] Confirm to yourself: how many hours/week will you actually give this after graduation? Write the number down.
- [ ] Confirm to yourself: are you willing to take a day job AND do this on nights/weekends? If not, either scale the plan down or don't start.
- [ ] Tell dad: this is a 3-month test, not a promise. Set expectations that success = 4-of-6 metrics from `01-mvp-spec.md`, not a running business.

## By end of week 1, you should have

1. A document with all camera/POS/portal details filled in.
2. A working Telegram bot that can send you a message from a Python script.
3. A cloud server (or Railway project) ready to deploy to.
4. A written personal commitment for time.
5. One day of downloaded CCTV footage from Cheap and Best salon on your laptop, ready for the week 2 walk-in-counting experiment.

Do not proceed to week 2 until all five are done. Discovery is not optional.
