"""
Base configuration model.
"""

from __future__ import annotations

from pydantic_settings import BaseSettings, SettingsConfigDict

from .constants import ENV_FILE, ENV_FILE_ENCODING


class BaseConfig(BaseSettings):
    """Base class for all configuration models."""

    model_config = SettingsConfigDict(
        env_file=ENV_FILE,
        env_file_encoding=ENV_FILE_ENCODING,
        extra="ignore",
        frozen=True,
        validate_default=True,
        case_sensitive=False,
    )
