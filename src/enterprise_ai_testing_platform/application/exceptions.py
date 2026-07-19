"""
Application layer exceptions.
"""

from enterprise_ai_testing_platform.exceptions import PlatformError


class ApplicationError(PlatformError):
    """
    Base exception for application layer failures.
    """
