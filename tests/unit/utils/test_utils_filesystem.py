"""
Tests for filesystem utilities.
"""

from pathlib import Path

from enterprise_ai_testing_platform.utils import ensure_directory


def test_ensure_directory_creates_directory(tmp_path: Path) -> None:
    """Verify ensure_directory creates the requested directory."""

    directory = tmp_path / "example"

    result = ensure_directory(directory)

    assert result.exists()
    assert result.is_dir()
