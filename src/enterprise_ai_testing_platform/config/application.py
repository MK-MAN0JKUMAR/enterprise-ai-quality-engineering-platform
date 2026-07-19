"""
Application configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .base import BaseConfig


class ApplicationSettings(BaseConfig):
    """Application metadata."""

    model_config = SettingsConfigDict(
        env_prefix="EATP_APP_",
    )

    name: str = Field(
        default="Enterprise AI Testing Platform",
        description="Application name.",
    )

    version: str = Field(
        default="0.1.0",
        description="Application version.",
    )
