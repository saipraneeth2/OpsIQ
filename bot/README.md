# bot/

The delivery layer. In v1, this is a Telegram bot; in v2, it graduates to WhatsApp Business API.

## Why start with Telegram

- Free. No approval flows, no per-message pricing.
- Bot creation is a 2-minute chat with @BotFather.
- Python client (`python-telegram-bot`) is mature and well-documented.
- Owners in India who don't use Telegram can install it in 30 seconds — but see the WhatsApp note below.

## Why WhatsApp is the eventual home

Indian franchise owners live on WhatsApp. Telegram is a founder-convenience shortcut, not the long-term product. Once the daily report is stable and one paying customer asks for WhatsApp, migrate — the report content stays identical, only the delivery channel changes.

## What lives here

- `telegram_bot.py` — the polling bot: handles `/start`, `/details`, `/staff`, `/anomalies` from the owner, delivers reports pushed from `backend/`.
- `whatsapp_client.py` (v2) — thin wrapper around Gupshup or Kaleyra (Meta-approved BSPs in India).

## Running the placeholder

```bash
cd bot
pip install python-telegram-bot
export OPSIQ_TELEGRAM_TOKEN=...    # from @BotFather
python telegram_bot.py
```
