"""
Base provider configuration.
"""

from __future__ import annotations

from pydantic import Field

from enterprise_ai_quality_engineering_platform.common import ProviderType

from ..base import BaseConfig
from .defaults import (
    DEFAULT_PROVIDER_MAX_RETRIES,
    DEFAULT_PROVIDER_TIMEOUT_SECONDS,
)


class ProviderConfig(BaseConfig):
    """
    Base configuration shared by all AI providers.

    Every provider-specific settings model should inherit from this class.
    """

    provider: ProviderType = Field(
        description="Provider identifier.",
    )

    enabled: bool = Field(
        default=True,
        description="Whether the provider is enabled.",
    )

    timeout_seconds: int = Field(
        default=DEFAULT_PROVIDER_TIMEOUT_SECONDS,
        ge=1,
        description="Request timeout in seconds.",
    )

    max_retries: int = Field(
        default=DEFAULT_PROVIDER_MAX_RETRIES,
        ge=0,
        description="Maximum retry attempts.",
    )
