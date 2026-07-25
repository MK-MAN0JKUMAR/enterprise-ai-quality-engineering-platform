"""
LM Studio provider constants.
"""

from enterprise_ai_quality_engineering_platform.providers.capabilities import (
    ProviderCapability,
)

PROVIDER_NAME = "lmstudio"

PROVIDER_VENDOR = "LM Studio"

PROVIDER_VERSION = "1.0"

SUPPORTED_CAPABILITIES: tuple[ProviderCapability, ...] = (ProviderCapability.CHAT,)
