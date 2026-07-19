from enterprise_ai_testing_platform.providers import (
    ProviderCapability,
)


def test_capability_values() -> None:
    assert ProviderCapability.CHAT == "chat"
    assert ProviderCapability.EMBEDDING == "embedding"
