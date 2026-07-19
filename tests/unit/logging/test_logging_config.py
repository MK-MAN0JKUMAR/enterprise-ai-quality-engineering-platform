"""
Tests for logging configuration models.
"""

from enterprise_ai_testing_platform.config.logging import LoggingSettings


def test_logging_settings_defaults() -> None:
    """Verify default logging configuration."""

    settings = LoggingSettings()

    assert settings.level == "INFO"
    assert settings.logger_name == "enterprise_ai_testing_platform"
    assert settings.console_enabled is True
    assert settings.file_enabled is False
    assert settings.log_directory == "logs"
    assert settings.file_name == "application.log"
