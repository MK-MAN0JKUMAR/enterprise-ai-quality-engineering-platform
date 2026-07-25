"""
Tests for Groq provider configuration.
"""

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config.providers import (
    GroqSettings,
)
from enterprise_ai_quality_engineering_platform.config.providers.defaults import (
    DEFAULT_GROQ_BASE_URL,
    DEFAULT_GROQ_CHAT_MODEL,
)


def test_groq_settings_defaults() -> None:
    """
    Verify default Groq configuration.
    """

    settings = GroqSettings()

    assert settings.provider is ProviderType.GROQ
    assert settings.enabled is True

    assert settings.base_url == DEFAULT_GROQ_BASE_URL

    assert settings.chat_model == DEFAULT_GROQ_CHAT_MODEL


def test_groq_settings_custom_values() -> None:
    """
    Verify custom Groq configuration.
    """

    settings = GroqSettings(
        enabled=False,
        api_key="test-key",
        base_url="https://example.com",
        chat_model="llama-test",
    )

    assert settings.provider is ProviderType.GROQ
    assert settings.enabled is False
    assert settings.api_key == "test-key"
    assert settings.base_url == "https://example.com"
    assert settings.chat_model == "llama-test"
