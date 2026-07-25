"""
Provider exceptions.
"""

from enterprise_ai_quality_engineering_platform.exceptions import PlatformError


class ProviderError(PlatformError):
    """
    Base exception for provider failures.
    """
