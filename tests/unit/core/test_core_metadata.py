from enterprise_ai_testing_platform.core.metadata import (
    PACKAGE_NAME,
    PROJECT_NAME,
    PYTHON_MIN_VERSION,
    VERSION,
)


def test_project_name() -> None:
    assert PROJECT_NAME == "Enterprise AI Testing Platform"


def test_package_name() -> None:
    assert PACKAGE_NAME == "enterprise_ai_testing_platform"


def test_version() -> None:
    assert VERSION == "0.1.0"


def test_python_version() -> None:
    assert PYTHON_MIN_VERSION == (3, 12)
