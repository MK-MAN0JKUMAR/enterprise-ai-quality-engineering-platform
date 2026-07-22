"""
Validation-related exceptions.
"""

from __future__ import annotations

from .base import PlatformError


class ValidationError(PlatformError):
    """Raised when validation fails."""
