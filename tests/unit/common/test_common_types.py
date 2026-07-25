"""
Tests for shared type aliases.
"""

from enterprise_ai_quality_engineering_platform.common.types import (
    JsonDict,
    JsonList,
    JsonValue,
)


def test_json_dict_alias() -> None:
    """Verify JsonDict alias."""

    value: JsonDict = {
        "name": "enterprise",
        "enabled": True,
    }

    assert value["name"] == "enterprise"


def test_json_list_alias() -> None:
    """Verify JsonList alias."""

    value: JsonList = [1, "two", True]

    assert len(value) == 3


def test_json_value_alias() -> None:
    """Verify JsonValue alias."""

    value: JsonValue = {
        "items": [1, 2, 3],
    }

    assert isinstance(value, dict)
