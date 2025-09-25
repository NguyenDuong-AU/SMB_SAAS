from dataclasses import dataclass
from typing import Annotated

from fastapi import Depends, Header, HTTPException, status


@dataclass(slots=True)
class TenantContext:
    """Context extracted from the incoming request identifying the tenant."""

    tenant_id: str
    acting_user_id: str | None = None


async def _get_tenant_id(x_tenant_id: Annotated[str | None, Header(alias="X-Tenant-ID")]) -> str:
    if not x_tenant_id:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail="X-Tenant-ID header is required to access tenant scoped resources.",
        )
    return x_tenant_id


async def _get_acting_user_id(x_user_id: Annotated[str | None, Header(alias="X-User-ID")]) -> str | None:
    return x_user_id


async def get_tenant_context(
    tenant_id: Annotated[str, Depends(_get_tenant_id)],
    acting_user_id: Annotated[str | None, Depends(_get_acting_user_id)],
) -> TenantContext:
    """Resolve the tenant context dependency for a request."""

    return TenantContext(tenant_id=tenant_id, acting_user_id=acting_user_id)
