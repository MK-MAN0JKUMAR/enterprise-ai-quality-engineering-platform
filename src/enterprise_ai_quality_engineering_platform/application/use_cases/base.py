"""
Application use case abstraction.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from enterprise_ai_quality_engineering_platform.application.context import ApplicationContext
from enterprise_ai_quality_engineering_platform.application.contracts import (
    ApplicationRequest,
    ApplicationResponse,
)


class UseCase(ABC):
    """
    Base class for all application use cases.
    """

    def __init__(self, context: ApplicationContext) -> None:
        """
        Initialize the use case.
        """

        self._context = context

    @property
    def context(self) -> ApplicationContext:
        """
        Return the application context.
        """

        return self._context

    @abstractmethod
    def execute(
        self,
        request: ApplicationRequest,
    ) -> ApplicationResponse:
        """
        Execute the use case.
        """
