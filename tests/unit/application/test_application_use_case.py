"""
Tests for application use cases.
"""

from enterprise_ai_testing_platform.application import (
    ApplicationContext,
    ApplicationRequest,
    ApplicationResponse,
    UseCase,
)
from enterprise_ai_testing_platform.services import ServiceContainer


class ExampleUseCase(UseCase):
    """
    Test use case.
    """

    def execute(
        self,
        request: ApplicationRequest,
    ) -> ApplicationResponse:
        return ApplicationResponse()


def test_use_case_exposes_context() -> None:
    """
    UseCase should expose its application context.
    """

    context = ApplicationContext(
        services=ServiceContainer(),
    )

    use_case = ExampleUseCase(context)

    assert use_case.context is context


def test_use_case_execute_returns_response() -> None:
    """
    UseCase implementation should return an ApplicationResponse.
    """

    context = ApplicationContext(
        services=ServiceContainer(),
    )

    use_case = ExampleUseCase(context)

    response = use_case.execute(ApplicationRequest())

    assert isinstance(response, ApplicationResponse)
