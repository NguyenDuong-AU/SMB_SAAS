from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration resolved from environment variables."""

    app_name: str = "SMB Automation Platform"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False

    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/smb_saas"
    redis_url: str = "redis://localhost:6379/0"

    allowed_origins: list[AnyHttpUrl] = []

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @field_validator("allowed_origins", mode="before")
    @classmethod
    def split_origins(cls, value: str | list[AnyHttpUrl] | None) -> list[AnyHttpUrl]:
        """Accept a comma separated list from environment variables."""
        if value is None or value == "":
            return []
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value


settings = Settings()
