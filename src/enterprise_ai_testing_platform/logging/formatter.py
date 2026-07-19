"""
Logging formatter definitions.
"""

from __future__ import annotations

import logging

from .constants import DEFAULT_DATE_FORMAT, DEFAULT_LOG_FORMAT


class PlatformFormatter(logging.Formatter):
    """Default formatter used throughout the platform."""

    def __init__(self) -> None:
        super().__init__(
            fmt=DEFAULT_LOG_FORMAT,
            datefmt=DEFAULT_DATE_FORMAT,
        )
