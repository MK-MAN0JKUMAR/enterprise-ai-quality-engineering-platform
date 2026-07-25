"""
Tests for provider base configuration.
"""

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config.providers import ProviderConfig
from enterprise_ai_quality_engineering_platform.config.providers.defaults import (
    DEFAULT_PROVIDER_MAX_RETRIES,
    DEFAULT_PROVIDER_TIMEOUT_SECONDS,
)


def test_provider_config_defaults() -> None:
    """
    ProviderConfig should use shared defaults.
    """

    config = ProviderConfig(
        provider=ProviderType.GROQ,
    )

    assert config.provider is ProviderType.GROQ
    assert config.enabled is True
    assert config.timeout_seconds == DEFAULT_PROVIDER_TIMEOUT_SECONDS
    assert config.max_retries == DEFAULT_PROVIDER_MAX_RETRIES


def test_provider_config_custom_values() -> None:
    """
    ProviderConfig should accept custom values.
    """

    config = ProviderConfig(
        provider=ProviderType.OLLAMA,
        enabled=False,
        timeout_seconds=120,
        max_retries=5,
    )

    assert config.provider is ProviderType.OLLAMA
    assert config.enabled is False
    assert config.timeout_seconds == 120
    assert config.max_retries == 5
