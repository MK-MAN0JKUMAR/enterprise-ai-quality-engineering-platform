"""
Application context.
"""

from __future__ import annotations

from dataclasses import dataclass

from enterprise_ai_quality_engineering_platform.services import ServiceContainer


@dataclass(slots=True)
class ApplicationContext:
    """
    Shared application execution context.

    Provides access to the platform service container used by
    application services and use cases.
    """

    services: ServiceContainer
