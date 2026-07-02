# backend/

FastAPI service — the single web app that owns the database, exposes an internal API for the vision worker and the bot, and hosts the scheduled report builder.

## Planned layout

```
backend/
├── main.py              # FastAPI app entrypoint
├── requirements.txt
├── app/
│   ├── config.py        # Pydantic settings, env-var loading
│   ├── db.py            # SQLAlchemy engine + session
│   ├── models/          # ORM models (tenant, store, sales, walkins, ...)
│   ├── schemas/         # Pydantic request/response schemas
│   ├── routers/         # FastAPI routers (health, stores, ingest, report)
│   ├── workers/         # Scheduled jobs (report_builder, pos_puller)
│   └── report/          # Report rendering (Markdown for Telegram)
├── alembic/             # DB migrations
└── tests/
```

Nothing to run yet — populate during Month 2 of the roadmap.

## Local dev (planned)

```bash
cd backend
pip install -r requirements.txt
cp ../.env.example ../.env  # fill in DB URL, telegram token, etc.
uvicorn main:app --reload
```
