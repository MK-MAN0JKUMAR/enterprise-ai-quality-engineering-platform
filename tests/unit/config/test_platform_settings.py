"""
Tests for platform settings.
"""

from enterprise_ai_testing_platform.config import (
    ApplicationSettings,
    PlatformSettings,
    RuntimeSettings,
)


def test_platform_settings_structure() -> None:
    """Verify composed settings."""

    platform_settings = PlatformSettings()

    assert isinstance(platform_settings.application, ApplicationSettings)
    assert isinstance(platform_settings.runtime, RuntimeSettings)
