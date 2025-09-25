from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.api.v1.endpoints import ping
from backend.app.core.config import settings

app = FastAPI(title=settings.app_name, debug=settings.debug)

if settings.allowed_origins:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.allowed_origins],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(ping.router, prefix=settings.api_v1_prefix)


@app.get("/health", tags=["health"])
async def health() -> dict[str, str]:
    """Non-tenant-specific health probe for infrastructure checks."""

    return {"status": "ok"}
