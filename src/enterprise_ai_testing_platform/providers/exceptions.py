"""
Provider exceptions.
"""

from enterprise_ai_testing_platform.exceptions import PlatformError


class ProviderError(PlatformError):
    """
    Base exception for provider failures.
    """
