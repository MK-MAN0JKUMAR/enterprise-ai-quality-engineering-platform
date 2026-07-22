"""
Tests for path validation utilities.
"""

from pathlib import Path

import pytest

from enterprise_ai_quality_engineering_platform.validation.paths import (
    validate_directory,
    validate_file,
    validate_path_exists,
)


def test_validate_path_exists(tmp_path: Path) -> None:
    """Validate an existing path."""

    assert validate_path_exists(tmp_path) == tmp_path


def test_validate_path_exists_missing(tmp_path: Path) -> None:
    """Raise for a missing path."""

    with pytest.raises(FileNotFoundError):
        validate_path_exists(tmp_path / "missing")


def test_validate_directory(tmp_path: Path) -> None:
    """Validate an existing directory."""

    assert validate_directory(tmp_path) == tmp_path


def test_validate_file(tmp_path: Path) -> None:
    """Validate an existing file."""

    file_path = tmp_path / "sample.txt"
    file_path.write_text("content")

    assert validate_file(file_path) == file_path
