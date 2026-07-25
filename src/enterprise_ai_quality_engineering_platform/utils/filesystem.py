"""
Filesystem utility functions.
"""

from __future__ import annotations

from pathlib import Path


def ensure_directory(path: Path | str) -> Path:
    """
    Ensure that a directory exists.

    If the directory does not exist, it is created along with any required
    parent directories.

    Args:
        path:
            Directory path.

    Returns:
        The resolved directory path.
    """

    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)

    return directory.resolve()
