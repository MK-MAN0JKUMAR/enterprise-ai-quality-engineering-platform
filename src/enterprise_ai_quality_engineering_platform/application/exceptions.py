"""
Application layer exceptions.
"""

from enterprise_ai_quality_engineering_platform.exceptions import PlatformError


class ApplicationError(PlatformError):
    """
    Base exception for application layer failures.
    """
