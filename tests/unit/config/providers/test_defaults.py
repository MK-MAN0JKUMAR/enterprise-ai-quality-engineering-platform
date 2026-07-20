"""
Tests for provider default values.
"""

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config.providers.defaults import (
    DEFAULT_CHAT_PROVIDER,
    DEFAULT_EMBEDDING_PROVIDER,
    DEFAULT_GROQ_BASE_URL,
    DEFAULT_GROQ_CHAT_MODEL,
    DEFAULT_OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_CHAT_MODEL,
    DEFAULT_OLLAMA_EMBEDDING_MODEL,
    DEFAULT_OLLAMA_RERANKING_MODEL,
    DEFAULT_PROVIDER_MAX_RETRIES,
    DEFAULT_PROVIDER_TIMEOUT_SECONDS,
    DEFAULT_RERANKING_PROVIDER,
)


def test_default_providers() -> None:
    """
    Verify default provider selections.
    """

    assert DEFAULT_CHAT_PROVIDER is ProviderType.GROQ
    assert DEFAULT_EMBEDDING_PROVIDER is ProviderType.OLLAMA
    assert DEFAULT_RERANKING_PROVIDER is ProviderType.OLLAMA


def test_default_retry_configuration() -> None:
    """
    Verify shared retry configuration.
    """

    assert DEFAULT_PROVIDER_TIMEOUT_SECONDS == 30
    assert DEFAULT_PROVIDER_MAX_RETRIES == 3


def test_default_groq_configuration() -> None:
    """
    Verify Groq defaults.
    """

    assert DEFAULT_GROQ_BASE_URL == "https://api.groq.com/openai/v1"

    assert DEFAULT_GROQ_CHAT_MODEL == "llama-3.3-70b-versatile"


def test_default_ollama_configuration() -> None:
    """
    Verify Ollama defaults.
    """

    assert DEFAULT_OLLAMA_BASE_URL == "http://localhost:11434"

    assert DEFAULT_OLLAMA_CHAT_MODEL == "llama3.1:8b"

    assert DEFAULT_OLLAMA_EMBEDDING_MODEL == "nomic-embed-text"

    assert DEFAULT_OLLAMA_RERANKING_MODEL == "bge-reranker-v2-m3"
