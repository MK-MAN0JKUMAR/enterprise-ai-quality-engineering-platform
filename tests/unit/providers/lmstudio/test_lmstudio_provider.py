"""
Tests for the LM Studio provider.
"""

from enterprise_ai_quality_engineering_platform.common import ProviderType
from enterprise_ai_quality_engineering_platform.config.providers import LMStudioSettings
from enterprise_ai_quality_engineering_platform.providers import LMStudioProvider
from enterprise_ai_quality_engineering_platform.providers.capabilities import (
    ProviderCapability,
)


def test_provider_metadata() -> None:
    """
    Provider metadata should be correct.
    """

    settings = LMStudioSettings()

    provider = LMStudioProvider(
        settings,
    )

    assert settings.provider is ProviderType.LMSTUDIO

    assert provider.metadata.name == "lmstudio"

    assert provider.metadata.vendor == "LM Studio"

    assert provider.metadata.version == "1.0"

    assert provider.metadata.capabilities == (ProviderCapability.CHAT,)


def test_provider_settings() -> None:
    """
    Provider should expose configuration.
    """

    settings = LMStudioSettings()

    provider = LMStudioProvider(
        settings,
    )

    assert provider.settings is settings


def test_provider_initialize() -> None:
    """
    Provider should initialize correctly.
    """

    provider = LMStudioProvider(
        LMStudioSettings(),
    )

    assert not provider.is_initialized

    provider.initialize()

    assert provider.is_initialized


def test_provider_shutdown() -> None:
    """
    Provider should shut down correctly.
    """

    provider = LMStudioProvider(
        LMStudioSettings(),
    )

    provider.initialize()

    assert provider.is_initialized

    provider.shutdown()

    assert not provider.is_initialized
