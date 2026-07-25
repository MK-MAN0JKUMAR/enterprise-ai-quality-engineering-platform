"""
Tests for application context.
"""

from enterprise_ai_quality_engineering_platform.application import ApplicationContext
from enterprise_ai_quality_engineering_platform.services import ServiceContainer


def test_application_context_stores_service_container() -> None:
    """
    ApplicationContext should expose the provided service container.
    """

    container = ServiceContainer()

    context = ApplicationContext(services=container)

    assert context.services is container
