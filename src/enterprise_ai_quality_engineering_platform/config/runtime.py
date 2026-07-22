"""
Runtime configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from .base import BaseConfig
from .constants import DEFAULT_ENVIRONMENT
from .environment import Environment


class RuntimeSettings(BaseConfig):
    """Runtime configuration."""

    model_config = SettingsConfigDict(
        env_prefix="EATP_RUNTIME_",
    )

    environment: Environment = Field(
        default=Environment(DEFAULT_ENVIRONMENT),
        description="Execution environment.",
    )

    debug: bool = Field(
        default=False,
        description="Enable debug mode.",
    )
