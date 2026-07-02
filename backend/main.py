"""OpsIq backend — FastAPI entrypoint.

Placeholder skeleton. The real implementation is scoped in
`docs/02-roadmap-90-days.md` (Month 2).
"""

from fastapi import FastAPI

app = FastAPI(
    title="OpsIq API",
    description="Multi-store operations platform for franchise owners.",
    version="0.0.1",
)


@app.get("/health")
async def health() -> dict[str, str]:
    """Liveness probe. Will return status of DB, worker, and bot in later versions."""
    return {"status": "ok", "service": "opsiq-backend"}


# TODO(month-2):
#   - Mount routers for /stores, /ingest/pos, /ingest/walkins, /reports
#   - Wire up async SQLAlchemy engine on startup
#   - Register APScheduler jobs (nightly vision worker, nightly POS pull, 9pm report)
#   - Add tenant_id middleware to enforce multi-tenant scoping on every query
