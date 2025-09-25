import os

from backend.app.core.config import Settings


def test_settings_allow_comma_separated_origins(monkeypatch):
    monkeypatch.setenv("ALLOWED_ORIGINS", "https://example.com, https://foo.dev")
    settings = Settings()
    assert settings.allowed_origins == [
        "https://example.com",
        "https://foo.dev",
    ]


def test_settings_override_database(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "postgresql+psycopg://user:pass@db:5432/app")
    settings = Settings()
    assert settings.database_url.endswith("app")
    assert "user:pass" in settings.database_url

    # ensure we did not mutate global settings
    assert os.getenv("DATABASE_URL") == "postgresql+psycopg://user:pass@db:5432/app"
