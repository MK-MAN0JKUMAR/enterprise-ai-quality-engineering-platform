"""
Tests for shared protocols.
"""

from enterprise_ai_quality_engineering_platform.common.protocols import (
    SupportsName,
)


class Example:
    """Example implementation."""

    @property
    def name(self) -> str:
        return "example"


def test_supports_name_protocol() -> None:
    """Verify protocol compatibility."""

    obj: SupportsName = Example()

    assert obj.name == "example"
