"""
LM Studio provider configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from enterprise_ai_quality_engineering_platform.common import ProviderType

from .base import ProviderConfig
from .defaults import (
    DEFAULT_LMSTUDIO_BASE_URL,
    DEFAULT_LMSTUDIO_CHAT_MODEL,
)
from .types import (
    BaseUrl,
    ModelName,
)


class LMStudioSettings(ProviderConfig):
    """
    Configuration for the LM Studio provider.
    """

    model_config = SettingsConfigDict(
        env_prefix="EATP_LMSTUDIO_",
    )

    provider: ProviderType = Field(
        default=ProviderType.LMSTUDIO,
    )

    base_url: BaseUrl = Field(
        default=DEFAULT_LMSTUDIO_BASE_URL,
        description="LM Studio API base URL.",
    )

    chat_model: ModelName = Field(
        default=DEFAULT_LMSTUDIO_CHAT_MODEL,
        description="Default LM Studio chat model.",
    )
