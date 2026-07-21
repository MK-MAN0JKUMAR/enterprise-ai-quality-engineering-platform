"""
Tests for GeminiProvider.
"""

from enterprise_ai_testing_platform.config.providers import GeminiSettings
from enterprise_ai_testing_platform.providers import (
    GeminiProvider,
    ProviderCapability,
)


def test_provider_metadata() -> None:
    provider = GeminiProvider(
        GeminiSettings(),
    )

    metadata = provider.metadata

    assert metadata.name == "gemini"
    assert metadata.vendor == "Google"
    assert metadata.version == "1.0"
    assert metadata.capabilities == (ProviderCapability.CHAT,)


def test_provider_settings() -> None:
    settings = GeminiSettings()

    provider = GeminiProvider(
        settings,
    )

    assert provider.settings is settings


def test_provider_lifecycle() -> None:
    provider = GeminiProvider(
        GeminiSettings(),
    )

    assert not provider.is_initialized

    provider.initialize()

    assert provider.is_initialized

    provider.shutdown()

    assert not provider.is_initialized
