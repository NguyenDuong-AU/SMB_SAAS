from datetime import datetime

from pydantic import BaseModel, Field


class TenantBase(BaseModel):
    name: str = Field(..., max_length=255)
    slug: str = Field(..., max_length=50)
    is_active: bool = True


class TenantCreate(TenantBase):
    id: str = Field(..., description="UUID assigned externally to allow BYOID migrations")


class TenantRead(TenantBase):
    id: str
    created_at: datetime


class UserBase(BaseModel):
    email: str
    full_name: str | None = None
    is_active: bool = True


class UserCreate(UserBase):
    id: str


class UserRead(UserBase):
    id: str
    created_at: datetime


class TenantUserRead(BaseModel):
    tenant_id: str
    user_id: str
    role: str
    is_default: bool
    created_at: datetime


class TenantWithUsers(TenantRead):
    users: list[TenantUserRead] = []

    model_config = {
        "from_attributes": True,
    }
