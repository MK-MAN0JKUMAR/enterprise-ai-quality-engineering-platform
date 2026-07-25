"""
Provider configuration aggregation.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from enterprise_ai_quality_engineering_platform.common import ProviderType

from ..base import BaseConfig
from .defaults import (
    DEFAULT_CHAT_PROVIDER,
    DEFAULT_EMBEDDING_PROVIDER,
    DEFAULT_RERANKING_PROVIDER,
)
from .gemini import GeminiSettings
from .groq import GroqSettings
from .lmstudio import LMStudioSettings
from .ollama import OllamaSettings


class ProviderSettings(BaseConfig):
    """
    Aggregate provider configuration.
    """

    model_config = SettingsConfigDict(
        env_prefix="EATP_PROVIDER_",
    )

    default_chat_provider: ProviderType = Field(
        default=DEFAULT_CHAT_PROVIDER,
        description="Default chat provider.",
    )

    default_embedding_provider: ProviderType = Field(
        default=DEFAULT_EMBEDDING_PROVIDER,
        description="Default embedding provider.",
    )

    default_reranking_provider: ProviderType = Field(
        default=DEFAULT_RERANKING_PROVIDER,
        description="Default reranking provider.",
    )

    groq: GroqSettings = Field(
        default_factory=GroqSettings,
    )

    ollama: OllamaSettings = Field(
        default_factory=OllamaSettings,
    )

    lmstudio: LMStudioSettings = Field(
        default_factory=LMStudioSettings,
    )

    gemini: GeminiSettings = Field(
        default_factory=GeminiSettings,
    )
