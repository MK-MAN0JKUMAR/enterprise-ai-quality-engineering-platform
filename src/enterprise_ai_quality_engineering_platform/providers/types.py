"""
Shared provider type definitions.
"""

from __future__ import annotations

from dataclasses import dataclass

from .capabilities import ProviderCapability


@dataclass(frozen=True, slots=True)
class ProviderMetadata:
    """
    Metadata describing a provider.
    """

    name: str

    vendor: str

    version: str

    capabilities: tuple[ProviderCapability, ...]
