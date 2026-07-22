"""
Logging configuration models.
"""

from __future__ import annotations

from pydantic import Field

from .base import BaseConfig


class LoggingSettings(BaseConfig):
    """Logging configuration."""

    level: str = Field(
        default="INFO",
        description="Default logging level.",
    )

    logger_name: str = Field(
        default="enterprise_ai_quality_engineering_platform",
        description="Root logger name.",
    )

    console_enabled: bool = Field(
        default=True,
        description="Enable console logging.",
    )

    file_enabled: bool = Field(
        default=False,
        description="Enable file logging.",
    )

    log_directory: str = Field(
        default="logs",
        description="Directory used for log files.",
    )

    file_name: str = Field(
        default="application.log",
        description="Default log file name.",
    )
