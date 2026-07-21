"""
Gemini provider configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from enterprise_ai_testing_platform.common import ProviderType

from .base import ProviderConfig
from .defaults import (
    DEFAULT_GEMINI_BASE_URL,
    DEFAULT_GEMINI_CHAT_MODEL,
)
from .types import (
    ApiKey,
    BaseUrl,
    ModelName,
)


class GeminiSettings(ProviderConfig):
    """
    Configuration for the Gemini provider.
    """

    model_config = SettingsConfigDict(
        env_prefix="EATP_GEMINI_",
    )

    provider: ProviderType = Field(
        default=ProviderType.GEMINI,
    )

    api_key: ApiKey = Field(
        default="",
        description="Gemini API key.",
    )

    base_url: BaseUrl = Field(
        default=DEFAULT_GEMINI_BASE_URL,
        description="Gemini API base URL.",
    )

    chat_model: ModelName = Field(
        default=DEFAULT_GEMINI_CHAT_MODEL,
        description="Default Gemini chat model.",
    )
