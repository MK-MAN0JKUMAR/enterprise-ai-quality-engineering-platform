"""
Tests for runtime settings.
"""

from enterprise_ai_quality_engineering_platform.config import Environment, RuntimeSettings


def test_runtime_defaults() -> None:
    """Verify runtime defaults."""

    runtime_settings = RuntimeSettings()

    assert runtime_settings.environment == Environment.DEVELOPMENT
    assert runtime_settings.debug is False
