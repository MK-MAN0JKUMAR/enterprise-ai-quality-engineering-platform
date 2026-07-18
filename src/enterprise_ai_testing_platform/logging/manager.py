"""
Logging configuration manager.
"""

from __future__ import annotations

import logging
from pathlib import Path

from enterprise_ai_testing_platform.config import get_settings
from enterprise_ai_testing_platform.utils import ensure_directory

from .formatter import PlatformFormatter


def configure_logging() -> logging.Logger:
    """
    Configure the platform logger.

    Returns:
        Configured logger.
    """

    settings = get_settings().logging

    logger = logging.getLogger(settings.logger_name)

    if logger.handlers:
        return logger

    level = getattr(logging, settings.level.upper(), logging.INFO)
    logger.setLevel(level)
    logger.propagate = False

    formatter = PlatformFormatter()

    if settings.console_enabled:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    if settings.file_enabled:
        log_directory = ensure_directory(settings.log_directory)
        log_file = Path(log_directory) / settings.file_name

        file_handler = logging.FileHandler(
            filename=log_file,
            encoding="utf-8",
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
