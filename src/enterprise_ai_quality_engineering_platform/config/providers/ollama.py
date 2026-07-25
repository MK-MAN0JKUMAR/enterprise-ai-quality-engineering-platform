"""
Ollama provider configuration.
"""

from __future__ import annotations

from pydantic import Field
from pydantic_settings import SettingsConfigDict

from enterprise_ai_quality_engineering_platform.common import ProviderType

from .base import ProviderConfig
from .defaults import (
    DEFAULT_OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_CHAT_MODEL,
    DEFAULT_OLLAMA_EMBEDDING_MODEL,
    DEFAULT_OLLAMA_RERANKING_MODEL,
)
from .types import (
    BaseUrl,
    ModelName,
)


class OllamaSettings(ProviderConfig):
    """
    Configuration for the Ollama provider.
    """

    model_config = SettingsConfigDict(
        env_prefix="EATP_OLLAMA_",
    )

    provider: ProviderType = Field(
        default=ProviderType.OLLAMA,
    )

    base_url: BaseUrl = Field(
        default=DEFAULT_OLLAMA_BASE_URL,
        description="Ollama server URL.",
    )

    chat_model: ModelName = Field(
        default=DEFAULT_OLLAMA_CHAT_MODEL,
        description="Default chat model.",
    )

    embedding_model: ModelName = Field(
        default=DEFAULT_OLLAMA_EMBEDDING_MODEL,
        description="Default embedding model.",
    )

    reranking_model: ModelName = Field(
        default=DEFAULT_OLLAMA_RERANKING_MODEL,
        description="Default reranking model.",
    )
