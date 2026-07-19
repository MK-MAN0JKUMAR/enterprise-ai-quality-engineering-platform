from enterprise_ai_testing_platform.core.runtime import (
    platform_name,
    python_version,
    runtime_metadata,
)


def test_python_version() -> None:
    assert isinstance(python_version(), str)


def test_platform_name() -> None:
    assert isinstance(platform_name(), str)


def test_runtime_metadata() -> None:
    metadata = runtime_metadata()

    assert metadata["project"] == "Enterprise AI Testing Platform"
    assert metadata["package"] == "enterprise_ai_testing_platform"
    assert "version" in metadata
    assert "python" in metadata
    assert "platform" in metadata
