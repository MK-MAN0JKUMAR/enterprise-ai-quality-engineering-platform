"""
Tests for GeminiSettings.
"""

from enterprise_ai_testing_platform.common import ProviderType
from enterprise_ai_testing_platform.config.providers import (
    GeminiSettings,
)
from enterprise_ai_testing_platform.config.providers.defaults import (
    DEFAULT_GEMINI_BASE_URL,
    DEFAULT_GEMINI_CHAT_MODEL,
)


def test_default_settings() -> None:
    settings = GeminiSettings()

    assert settings.provider == ProviderType.GEMINI
    assert settings.enabled is True
    assert settings.base_url == DEFAULT_GEMINI_BASE_URL
    assert settings.chat_model == DEFAULT_GEMINI_CHAT_MODEL
    assert settings.timeout_seconds == 30
    assert settings.max_retries == 3
