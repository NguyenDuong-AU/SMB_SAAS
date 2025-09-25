# SMB Automation SaaS

This repository contains the foundational building blocks for a modular, multi-tenant SaaS targeting small and medium
businesses. The goal is to deliver boring-but-profitable automations that improve speed-to-lead, reduce no-shows, and
accelerate revenue collection.

## Project Structure

```
backend/
  app/
    api/            # FastAPI routers grouped by version
    core/           # Configuration, tenancy helpers, middleware
    db/             # SQLAlchemy session and base classes
    models/         # ORM models (Tenants, Users, Associations)
    schemas/        # Pydantic schemas for API I/O
    main.py         # FastAPI application entrypoint
```

## Getting Started

1. **Create and activate a Python virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -e .[test]
   ```

3. **Run the FastAPI app locally**
   ```bash
   uvicorn backend.app.main:app --reload
   ```
   The service exposes:
   - `GET /health` – infrastructure health probe (no tenant required).
   - `GET /api/v1/ping` – tenant-aware readiness check requiring an `X-Tenant-ID` header.

4. **Run tests**
   ```bash
   pytest
   ```

## Manual Testing

To exercise the tenant-aware dependency manually once the server is running, you can use `curl`:

```bash
curl -H "X-Tenant-ID: demo-tenant" http://127.0.0.1:8000/api/v1/ping
```

Expected response:

```json
{"status": "ok", "tenant_id": "demo-tenant"}
```

If the header is missing, the API will respond with `422 Unprocessable Entity`, confirming that tenant context is
mandatory for scoped endpoints.

## Next Steps

- Wire the ORM models to migrations and persistence.
- Implement OAuth2/OIDC authentication and RBAC policies.
- Add messaging adapters (email, SMS) and event bus integration.
- Expand module-specific APIs following the blueprint specification.
