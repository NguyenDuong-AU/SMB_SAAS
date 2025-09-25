import pytest
from fastapi import status
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_ping_requires_tenant_header():
    response = client.get("/api/v1/ping")
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY
    assert response.json()["detail"] == "X-Tenant-ID header is required to access tenant scoped resources."


def test_ping_returns_tenant_id():
    response = client.get("/api/v1/ping", headers={"X-Tenant-ID": "tenant-123"})
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "ok", "tenant_id": "tenant-123"}


@pytest.mark.parametrize(
    "tenant_id,user_id",
    [
        ("tenant-1", None),
        ("tenant-2", "user-abc"),
    ],
)
def test_tenant_context_optional_user_id(tenant_id: str, user_id: str | None):
    headers = {"X-Tenant-ID": tenant_id}
    if user_id:
        headers["X-User-ID"] = user_id

    response = client.get("/api/v1/ping", headers=headers)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["tenant_id"] == tenant_id
