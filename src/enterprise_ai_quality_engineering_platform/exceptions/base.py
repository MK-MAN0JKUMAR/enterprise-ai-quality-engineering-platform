"""
Base exception hierarchy for the Enterprise AI Quality Engineering Platform.
"""

from __future__ import annotations


class PlatformError(Exception):
    """Base exception for all platform-specific errors."""


class PlatformRuntimeError(PlatformError):
    """Raised for unrecoverable runtime errors."""
