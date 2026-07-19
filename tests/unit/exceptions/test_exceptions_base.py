from enterprise_ai_testing_platform.exceptions import (
    ConfigurationError,
    PlatformError,
    PlatformRuntimeError,
    PluginError,
    ProviderError,
    ValidationError,
)


def test_platform_error_inheritance() -> None:
    assert issubclass(PlatformRuntimeError, PlatformError)
    assert issubclass(ConfigurationError, PlatformError)
    assert issubclass(ValidationError, PlatformError)
    assert issubclass(ProviderError, PlatformError)
    assert issubclass(PluginError, PlatformError)


def test_platform_error_instance() -> None:
    error = PlatformError("platform error")
    assert str(error) == "platform error"
