from typing import Any

from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    """Declarative base that automatically configures table names and metadata."""

    id: Any
    __name__: str

    @declared_attr.directive
    def __tablename__(cls) -> str:  # type: ignore[misc]
        return cls.__name__.lower()

    @declared_attr.directive
    def __table_args__(cls) -> tuple[dict[str, Any], ...]:  # type: ignore[misc]
        return ({"schema": "public"},)
