"""
Tests for application settings.
"""

from enterprise_ai_quality_engineering_platform.config import ApplicationSettings


def test_application_defaults() -> None:
    """Verify application defaults."""

    application_settings = ApplicationSettings()

    assert application_settings.name == "Enterprise AI Quality Engineering Platform"
    assert application_settings.version == "0.1.0"
