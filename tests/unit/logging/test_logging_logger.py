"""
Tests for logger factory.
"""

import logging

from enterprise_ai_testing_platform.logging import get_logger
from enterprise_ai_testing_platform.logging.constants import (
    DEFAULT_LOGGER_NAME,
)


def test_get_default_logger() -> None:
    """Verify default logger."""

    logger = get_logger()

    assert isinstance(logger, logging.Logger)
    assert logger.name == DEFAULT_LOGGER_NAME


def test_get_named_logger() -> None:
    """Verify named logger."""

    logger = get_logger("tests.logger")

    assert isinstance(logger, logging.Logger)
    assert logger.name == "tests.logger"
