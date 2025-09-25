from fastapi import APIRouter, Depends

from backend.app.core.tenancy import TenantContext, get_tenant_context

router = APIRouter(tags=["health"])


@router.get("/ping")
async def ping(tenant: TenantContext = Depends(get_tenant_context)) -> dict[str, str]:
    """Simple tenant-aware readiness endpoint."""

    return {"status": "ok", "tenant_id": tenant.tenant_id}
