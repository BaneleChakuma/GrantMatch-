# GrantMatch

GrantMatch orchestrates scholarship matching, identity verification, enrollment checks, and disbursement across African fintech APIs — closing the gap from *eligible* to *paid* with a full audit trail.

**Capstone focus:** System integration + QA testing.

- [GitHub Project board](https://github.com/users/BaneleChakuma/projects/1)
- [Issue #1 — Initialize repo](https://github.com/BaneleChakuma/GrantMatch-/issues/1)

## Tech stack

| Layer | Technology |
|-------|------------|
| API | Python 3.12, FastAPI |
| Database | PostgreSQL 16 |
| Frontend | React, TypeScript, Vite |
| Mock SIS (Month 3) | Java, Spring Boot |
| Local dev | Docker Compose |

## Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Python 3.12+
- Node.js 20+

## Quick start

### 1. Environment

```bash
cp .env.example .env
```

### 2. API + database (Docker)

```bash
docker compose up --build
```

- API docs: http://localhost:8000/docs
- PostgreSQL: `localhost:5432` (user/pass/db: `grantmatch`)

### 3. Frontend (local)

```bash
cd web
npm install
npm run dev
```

- Web app: http://localhost:5173

### 4. Run tests

```bash
cd apps/api
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Repository layout

```
apps/api/          FastAPI backend
web/               React + Vite frontend
services/mock-sis/ Java Mock University SIS (Month 3)
```

## License

MIT — see [LICENSE](LICENSE).
