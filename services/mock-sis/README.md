# Mock University SIS (Month 3)

**Java + Spring Boot** microservice that simulates a university Student Information System.

GrantMatch (Python/FastAPI) will call this service and receive enrollment webhooks — demonstrating **polyglot system integration** without needing real campus API access.

## Planned endpoints (M3-2)

| Method | Path | Purpose |
|--------|------|---------|
| `GET` | `/api/v1/enrollment/{studentId}` | Returns `ENROLLED` or `NOT_ENROLLED` |
| `POST` | `/api/v1/webhooks/simulate-enrollment` | Triggers webhook to GrantMatch |

Default port: **8081** (see root `.env.example` when added in Month 3).

## Why Java here?

- Uses WeThinkCode Java skills in a focused second service
- Shows integration **across languages**, not only REST within one stack
- Keeps payment orchestration in Python/FastAPI where webhooks and async fit well

The main GrantMatch API remains **Python/FastAPI**.
