# QueryLens Backend and Infrastructure

This repository contains the FastAPI service, SQL analysis and validation, read-only PostgreSQL access, tests, database initialization scripts, and Docker Compose configuration. Phase 1 provides a local fictional database with 100,000 sales and query plan analysis.

## Requirements

- Docker Desktop with Docker Compose.
- The `querylens-frontend` repository as a sibling folder to build the complete application.
- To run components outside Docker: Python 3.13; Node.js 20.19 or later for the frontend.

## Clone the repositories

Clone both repositories into `QueryLensWorkspace` so they are sibling folders:

```powershell
git clone https://github.com/querylens-labs/querylens-frontend.git
git clone https://github.com/querylens-labs/querylens-backend.git
cd querylens-backend
```

If you have opened `QueryLens.code-workspace`, you can run these commands in its integrated terminal.

## Run the complete application

From the root of `querylens-backend`, in PowerShell:

```powershell
Copy-Item .env.example .env
docker compose up --build -d
```

Open <http://localhost:3000>. Compose builds the backend from this repository and the frontend from `../querylens-frontend`; Nginx forwards `/api` to FastAPI. PostgreSQL initializes the schema and fictional data when it creates the volume for the first time.

Check service status and demo data:

```powershell
docker compose ps
docker compose exec db psql -U querylens_admin -d querylens -c "SELECT count(*) AS sales FROM sales;"
```

Initialization scripts run only when the volume is empty. Removing the volume deletes the local demo data.

## Run components outside Docker

Start PostgreSQL with Compose, then configure the API with `QUERYLENS_DB_HOST=localhost`, `QUERYLENS_DB_PORT` from `.env` (55432 in `.env.example`), `QUERYLENS_DB_NAME=querylens`, `QUERYLENS_DB_USER=querylens_readonly`, and `QUERYLENS_DB_PASSWORD` from `.env`.

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
uvicorn app.main:app --reload --port 8000
```

In a second terminal, from `../querylens-frontend`:

```powershell
npm ci
npm run dev
```

Vite serves the frontend at <http://localhost:5173> and proxies `/api` to <http://localhost:8000>.

## API and security

- `GET /api/health`: FastAPI and PostgreSQL connection status.
- `POST /api/analyze`: accepts `{"query": "SELECT ..."}` and returns timings and plan nodes.
- `/docs`: FastAPI interactive documentation.

The API accepts one `SELECT` statement (including `WITH ... SELECT`) in a read-only transaction with a 10-second timeout. `EXPLAIN ANALYZE` executes the query; use only the local demo database. The API user has `SELECT` permissions only on the configured tables. Values in `.env.example` are for local development and must not be used when exposing services.

## Tests

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest
```

## Workspace and project instructions

Open `QueryLens.code-workspace` in VS Code to load both repositories as separate folders and Git repositories. Project rules are in `AGENTS.md`; Claude Code should read `CLAUDE.md`. The custom QueryLens agent is in `.github/agents/querylens.agent.md`.

The expected workspace contains exactly two sibling folders: `querylens-frontend` (https://github.com/QueryLens-labs/querylens-frontend) and `querylens-backend`.

The QueryLens roadmap is maintained in [TODO.md](TODO.md).

## License

Copyright (c) 2026 J0x1N. All rights reserved.

QueryLens is a personally owned project. Its source code
is publicly available for viewing, but no open-source
license is granted.

Unauthorized use, modification, or redistribution of
the source code is not permitted, except as allowed by
applicable law or GitHub's Terms of Service.
