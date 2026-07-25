"""
Tests for Ollama provider configuration.
"""

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config.providers import OllamaSettings
from enterprise_ai_quality_engineering_platform.config.providers.defaults import (
    DEFAULT_OLLAMA_BASE_URL,
    DEFAULT_OLLAMA_CHAT_MODEL,
    DEFAULT_OLLAMA_EMBEDDING_MODEL,
    DEFAULT_OLLAMA_RERANKING_MODEL,
)


def test_ollama_settings_defaults() -> None:
    """
    Verify default Ollama configuration.
    """

    settings = OllamaSettings()

    assert settings.provider is ProviderType.OLLAMA
    assert settings.enabled is True

    assert settings.base_url == DEFAULT_OLLAMA_BASE_URL
    assert settings.chat_model == DEFAULT_OLLAMA_CHAT_MODEL
    assert settings.embedding_model == DEFAULT_OLLAMA_EMBEDDING_MODEL
    assert settings.reranking_model == DEFAULT_OLLAMA_RERANKING_MODEL


def test_ollama_settings_custom_values() -> None:
    """
    Verify custom Ollama configuration.
    """

    settings = OllamaSettings(
        enabled=False,
        base_url="http://test:11434",
        chat_model="llama-test",
        embedding_model="embed-test",
        reranking_model="rerank-test",
    )

    assert settings.provider is ProviderType.OLLAMA
    assert settings.enabled is False

    assert settings.base_url == "http://test:11434"
    assert settings.chat_model == "llama-test"
    assert settings.embedding_model == "embed-test"
    assert settings.reranking_model == "rerank-test"
