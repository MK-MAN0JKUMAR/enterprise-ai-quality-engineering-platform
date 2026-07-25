"""
Tests for logging manager.
"""

import logging

from enterprise_ai_quality_engineering_platform.logging.manager import (
    configure_logging,
)


def test_configure_logging_returns_logger() -> None:
    """Verify logger configuration."""

    logger = configure_logging()

    assert isinstance(logger, logging.Logger)


def test_configure_logging_is_idempotent() -> None:
    """Verify repeated configuration does not duplicate handlers."""

    logger = configure_logging()

    handler_count = len(logger.handlers)

    configure_logging()

    assert len(logger.handlers) == handler_count
