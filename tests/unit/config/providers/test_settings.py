"""
Tests for provider settings.
"""

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config.providers import (
    GroqSettings,
    OllamaSettings,
    ProviderSettings,
)
from enterprise_ai_testing_platform.config.providers.defaults import (
    DEFAULT_CHAT_PROVIDER,
    DEFAULT_EMBEDDING_PROVIDER,
    DEFAULT_RERANKING_PROVIDER,
)
from enterprise_ai_testing_platform.config.providers.lmstudio import LMStudioSettings


def test_provider_settings_defaults() -> None:
    """
    Verify provider settings defaults.
    """

    settings = ProviderSettings()

    assert settings.default_chat_provider is DEFAULT_CHAT_PROVIDER

    assert settings.default_embedding_provider is DEFAULT_EMBEDDING_PROVIDER

    assert settings.default_reranking_provider is DEFAULT_RERANKING_PROVIDER


def test_provider_settings_nested_models() -> None:
    """
    Verify nested provider models.
    """

    settings = ProviderSettings()

    assert isinstance(
        settings.groq,
        GroqSettings,
    )

    assert isinstance(
        settings.ollama,
        OllamaSettings,
    )

    assert isinstance(
        settings.lmstudio,
        LMStudioSettings,
    )


def test_provider_settings_custom_defaults() -> None:
    """
    Verify overriding default providers.
    """

    settings = ProviderSettings(
        default_chat_provider=ProviderType.OLLAMA,
        default_embedding_provider=ProviderType.GROQ,
        default_reranking_provider=ProviderType.GROQ,
    )

    assert settings.default_chat_provider is ProviderType.OLLAMA

    assert settings.default_embedding_provider is ProviderType.GROQ

    assert settings.default_reranking_provider is ProviderType.GROQ

    assert settings.lmstudio.provider is ProviderType.LMSTUDIO
