"""
Tests for configuration loader.
"""

from enterprise_ai_testing_platform.config import PlatformSettings, get_settings


def test_loader_returns_singleton() -> None:
    """Verify cached singleton."""

    first = get_settings()
    second = get_settings()

    assert isinstance(first, PlatformSettings)
    assert first is second
