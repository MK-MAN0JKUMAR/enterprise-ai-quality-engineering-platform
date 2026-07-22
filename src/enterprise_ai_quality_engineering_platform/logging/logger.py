"""
Logger factory functions.
"""

from __future__ import annotations

import logging

from .constants import DEFAULT_LOGGER_NAME


def get_logger(name: str | None = None) -> logging.Logger:
    """
    Return a configured logger.

    Args:
        name:
            Logger name.

    Returns:
        Logger instance.
    """

    return logging.getLogger(name or DEFAULT_LOGGER_NAME)
