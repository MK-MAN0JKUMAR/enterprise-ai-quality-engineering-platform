"""
Application service abstraction.
"""

from __future__ import annotations

from enterprise_ai_quality_engineering_platform.application.context import ApplicationContext


class ApplicationService:
    """
    Base class for all application services.
    """

    def __init__(self, context: ApplicationContext) -> None:
        """
        Initialize the application service.
        """

        self._context = context

    @property
    def context(self) -> ApplicationContext:
        """
        Return the application context.
        """

        return self._context
