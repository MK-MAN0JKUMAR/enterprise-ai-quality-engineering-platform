"""
Tests for file validation utilities.
"""

from pathlib import Path

import pytest

from enterprise_ai_quality_engineering_platform.validation.files import (
    validate_extension,
    validate_file_size,
    validate_non_empty_file,
)


def test_validate_extension(tmp_path: Path) -> None:
    """Validate file extension."""

    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello")

    assert validate_extension(file_path, ".txt") == file_path


def test_validate_extension_invalid(tmp_path: Path) -> None:
    """Reject invalid extension."""

    file_path = tmp_path / "sample.json"
    file_path.write_text("{}")

    with pytest.raises(ValueError):
        validate_extension(file_path, ".txt")


def test_validate_file_size(tmp_path: Path) -> None:
    """Validate file size."""

    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello")

    assert (
        validate_file_size(
            file_path,
            max_size_bytes=100,
        )
        == file_path
    )


def test_validate_non_empty_file(tmp_path: Path) -> None:
    """Validate non-empty file."""

    file_path = tmp_path / "sample.txt"
    file_path.write_text("hello")

    assert validate_non_empty_file(file_path) == file_path
