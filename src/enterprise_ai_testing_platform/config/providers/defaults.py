"""
Default provider configuration values.
"""

from __future__ import annotations

from typing import Final

from enterprise_ai_testing_platform.common import ProviderType

from .types import (
    BaseUrl,
    ModelName,
)

# --------------------------
# Default provider selection
# --------------------------

DEFAULT_CHAT_PROVIDER: Final = ProviderType.GROQ

DEFAULT_EMBEDDING_PROVIDER: Final = ProviderType.OLLAMA

DEFAULT_RERANKING_PROVIDER: Final = ProviderType.OLLAMA

# --------------------------
# Shared defaults
# --------------------------

DEFAULT_PROVIDER_TIMEOUT_SECONDS: Final = 30

DEFAULT_PROVIDER_MAX_RETRIES: Final = 3

# --------------------------
# Groq defaults
# --------------------------

DEFAULT_GROQ_BASE_URL: Final[BaseUrl] = "https://api.groq.com/openai/v1"

DEFAULT_GROQ_CHAT_MODEL: Final[ModelName] = "llama-3.3-70b-versatile"

# --------------------------
# Gemini defaults
# --------------------------

DEFAULT_GEMINI_BASE_URL: Final[BaseUrl] = "https://generativelanguage.googleapis.com/v1beta"

DEFAULT_GEMINI_CHAT_MODEL: Final[ModelName] = "gemini-2.5-flash"


# --------------------------
# LM Studio defaults
# --------------------------

DEFAULT_LMSTUDIO_BASE_URL: Final[BaseUrl] = "http://localhost:1234/v1"

DEFAULT_LMSTUDIO_CHAT_MODEL: Final[ModelName] = "local-model"


# --------------------------
# Ollama defaults
# --------------------------

DEFAULT_OLLAMA_BASE_URL: Final[BaseUrl] = "http://localhost:11434"

DEFAULT_OLLAMA_CHAT_MODEL: Final[ModelName] = "llama3.1:8b"

DEFAULT_OLLAMA_EMBEDDING_MODEL: Final[ModelName] = "nomic-embed-text"

DEFAULT_OLLAMA_RERANKING_MODEL: Final[ModelName] = "bge-reranker-v2-m3"
