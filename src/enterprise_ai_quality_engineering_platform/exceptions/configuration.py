"""
Configuration-related exceptions.
"""

from __future__ import annotations

from .base import PlatformError


class ConfigurationError(PlatformError):
    """Raised when configuration is invalid or missing."""
