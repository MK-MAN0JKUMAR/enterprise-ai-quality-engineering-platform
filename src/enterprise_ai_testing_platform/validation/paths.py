"""
Filesystem path validation utilities.
"""

from pathlib import Path


def validate_path_exists(path: str | Path) -> Path:
    """
    Validate that a path exists.

    Args:
        path: Path to validate.

    Returns:
        Validated path.

    Raises:
        FileNotFoundError:
            If the path does not exist.
    """

    resolved = Path(path)

    if not resolved.exists():
        raise FileNotFoundError(f"Path does not exist: {resolved}")

    return resolved


def validate_directory(path: str | Path) -> Path:
    """
    Validate that a directory exists.

    Args:
        path: Directory path.

    Returns:
        Validated directory path.

    Raises:
        NotADirectoryError:
            If the path is not a directory.
    """

    directory = validate_path_exists(path)

    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    return directory


def validate_file(path: str | Path) -> Path:
    """
    Validate that a file exists.

    Args:
        path: File path.

    Returns:
        Validated file path.

    Raises:
        FileNotFoundError:
            If the file does not exist.
    """

    file_path = validate_path_exists(path)

    if not file_path.is_file():
        raise FileNotFoundError(f"Not a file: {file_path}")

    return file_path
