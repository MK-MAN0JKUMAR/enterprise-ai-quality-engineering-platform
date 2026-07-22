from enterprise_ai_quality_engineering_platform.providers import (
    Provider,
    ProviderCapability,
    ProviderMetadata,
)


class DummyProvider(Provider):
    def __init__(self) -> None:
        self._initialized = False

    @property
    def metadata(self) -> ProviderMetadata:
        return ProviderMetadata(
            name="dummy",
            vendor="test",
            version="1.0",
            capabilities=(ProviderCapability.CHAT,),
        )

    def initialize(self) -> None:
        self._initialized = True

    def shutdown(self) -> None:
        self._initialized = False

    @property
    def is_initialized(self) -> bool:
        return self._initialized


def test_provider_lifecycle() -> None:
    provider = DummyProvider()

    assert not provider.is_initialized

    provider.initialize()

    assert provider.is_initialized

    provider.shutdown()

    assert not provider.is_initialized
