"""
Tests for LM Studio provider configuration.
"""

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config.providers import LMStudioSettings


def test_lmstudio_settings_defaults() -> None:
    """
    LM Studio settings should expose expected defaults.
    """

    settings = LMStudioSettings()

    assert settings.provider is ProviderType.LMSTUDIO

    assert settings.base_url == "http://localhost:1234/v1"

    assert settings.chat_model == "local-model"
