"""
Provider-related exceptions.
"""

from __future__ import annotations

from .base import PlatformError


class ProviderError(PlatformError):
    """Base exception for provider implementations."""
