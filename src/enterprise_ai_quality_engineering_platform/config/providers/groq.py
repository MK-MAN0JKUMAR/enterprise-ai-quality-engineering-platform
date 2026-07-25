"""
Groq provider configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from enterprise_ai_quality_engineering_platform.common import ProviderType

from .base import ProviderConfig
from .defaults import (
    DEFAULT_GROQ_BASE_URL,
    DEFAULT_GROQ_CHAT_MODEL,
)
from .types import (
    ApiKey,
    BaseUrl,
    ModelName,
)


class GroqSettings(ProviderConfig):
    """
    Configuration for the Groq provider.
    """

    model_config = SettingsConfigDict(
        env_prefix="EATP_GROQ_",
    )

    provider: ProviderType = Field(
        default=ProviderType.GROQ,
    )

    api_key: ApiKey = Field(
        default="",
        description="Groq API key.",
    )

    base_url: BaseUrl = Field(
        default=DEFAULT_GROQ_BASE_URL,
        description="Groq API base URL.",
    )

    chat_model: ModelName = Field(
        default=DEFAULT_GROQ_CHAT_MODEL,
        description="Default chat model.",
    )
