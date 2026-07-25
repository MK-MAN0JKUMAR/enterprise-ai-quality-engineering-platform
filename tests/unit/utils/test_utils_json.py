"""
Tests for JSON utilities.
"""

from __future__ import annotations

from pathlib import Path

from enterprise_ai_quality_engineering_platform.utils import (
    read_json_file,
    write_json_file,
)


def test_write_and_read_json_file(tmp_path: Path) -> None:
    """Verify JSON can be written and read successfully."""

    file_path = tmp_path / "sample.json"

    expected = {
        "name": "Enterprise AI Quality Engineering Platform",
        "version": "0.1.0",
    }

    write_json_file(file_path, expected)

    actual = read_json_file(file_path)

    assert actual == expected
