from enterprise_ai_quality_engineering_platform.providers import (
    ProviderCapability,
)


def test_capability_values() -> None:
    assert ProviderCapability.CHAT == "chat"
    assert ProviderCapability.EMBEDDING == "embedding"
