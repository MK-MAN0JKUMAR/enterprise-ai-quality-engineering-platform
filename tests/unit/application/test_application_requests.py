"""
Tests for application requests.
"""

from enterprise_ai_testing_platform.application import ApplicationRequest


def test_application_request_defaults() -> None:
    """
    ApplicationRequest should initialize with empty metadata.
    """

    request = ApplicationRequest()

    assert request.metadata == {}
