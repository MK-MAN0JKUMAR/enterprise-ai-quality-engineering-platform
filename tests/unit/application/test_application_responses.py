"""
Tests for application responses.
"""

from enterprise_ai_testing_platform.application import ApplicationResponse


def test_application_response_defaults() -> None:
    """
    ApplicationResponse should initialize with default values.
    """

    response = ApplicationResponse()

    assert response.success is True
    assert response.metadata == {}
