"""
Tests for application services.
"""

from enterprise_ai_quality_engineering_platform.application import (
    ApplicationContext,
    ApplicationService,
)
from enterprise_ai_quality_engineering_platform.services import ServiceContainer


class ExampleService(ApplicationService):
    """
    Test application service.
    """


def test_application_service_exposes_context() -> None:
    """
    ApplicationService should expose its application context.
    """

    context = ApplicationContext(
        services=ServiceContainer(),
    )

    service = ExampleService(context)

    assert service.context is context
