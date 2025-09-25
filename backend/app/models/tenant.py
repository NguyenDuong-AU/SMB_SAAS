from __future__ import annotations

from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Boolean, DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app.db.base_class import Base

if TYPE_CHECKING:  # pragma: no cover
    from sqlalchemy.orm import RelationshipProperty


class Tenant(Base):
    """Represents a company/account that uses the SaaS platform."""

    __tablename__ = "tenants"

    id: Mapped[str] = mapped_column(String(length=36), primary_key=True)
    name: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    slug: Mapped[str] = mapped_column(String(length=50), unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    users: Mapped[list["TenantUser"]] = relationship(back_populates="tenant", cascade="all, delete-orphan")


class User(Base):
    """Represents a person that can log into the platform."""

    __tablename__ = "users"

    id: Mapped[str] = mapped_column(String(length=36), primary_key=True)
    email: Mapped[str] = mapped_column(String(length=255), unique=True, nullable=False)
    full_name: Mapped[str] = mapped_column(String(length=255), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    tenants: Mapped[list["TenantUser"]] = relationship(back_populates="user", cascade="all, delete-orphan")


class TenantUser(Base):
    """Association table storing the role of a user inside a tenant."""

    __tablename__ = "tenant_users"
    __table_args__ = (UniqueConstraint("tenant_id", "user_id", name="uq_tenant_user"),)

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tenant_id: Mapped[str] = mapped_column(ForeignKey("public.tenants.id", ondelete="CASCADE"), nullable=False)
    user_id: Mapped[str] = mapped_column(ForeignKey("public.users.id", ondelete="CASCADE"), nullable=False)
    role: Mapped[str] = mapped_column(String(length=50), nullable=False, default="staff")
    is_default: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), default=datetime.utcnow)

    tenant: Mapped["Tenant"] = relationship(back_populates="users")
    user: Mapped["User"] = relationship(back_populates="tenants")
