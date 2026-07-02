"""OpsIq Telegram bot — placeholder.

Real implementation lands in Week 8. For Week 1, this file exists so you
can smoke-test message delivery: replace the token, set your chat id,
and run to confirm you can send yourself a message from Python.

Usage (Week 1 smoke test):

    export OPSIQ_TELEGRAM_TOKEN=<from @BotFather>
    export OPSIQ_OWNER_CHAT_ID=<your telegram chat id>
    python telegram_bot.py
"""

from __future__ import annotations

import asyncio
import os

# In Week 1 you can use a minimal HTTP call without installing python-telegram-bot:
#   curl -X POST "https://api.telegram.org/bot<TOKEN>/sendMessage" \
#        -d chat_id=<CHAT_ID> -d text="hello from opsiq"
# But once the real bot is built, we use python-telegram-bot for the polling loop.


async def send_smoke_test() -> None:
    token = os.environ.get("OPSIQ_TELEGRAM_TOKEN")
    chat_id = os.environ.get("OPSIQ_OWNER_CHAT_ID")
    if not token or not chat_id:
        print(
            "Set OPSIQ_TELEGRAM_TOKEN and OPSIQ_OWNER_CHAT_ID env vars first. "
            "See docs/06-week-1-checklist.md."
        )
        return

    import httpx  # only imported when actually running

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": "hello from opsiq — delivery layer smoke test ok",
    }
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.post(url, data=payload)
        r.raise_for_status()
        print("[opsiq.bot] smoke test message sent.")


if __name__ == "__main__":
    asyncio.run(send_smoke_test())
