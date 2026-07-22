"""
File validation utilities.
"""

from pathlib import Path


def validate_extension(path: str | Path, *extensions: str) -> Path:
    """
    Validate a file extension.

    Args:
        path: File path.
        extensions: Allowed extensions.

    Returns:
        Validated file path.

    Raises:
        ValueError:
            If the extension is invalid.
    """

    file_path = Path(path)

    if file_path.suffix.lower() not in {extension.lower() for extension in extensions}:
        raise ValueError(f"Unsupported file extension: {file_path.suffix}")

    return file_path


def validate_file_size(
    path: str | Path,
    *,
    max_size_bytes: int,
) -> Path:
    """
    Validate file size.

    Args:
        path: File path.
        max_size_bytes: Maximum allowed size.

    Returns:
        Validated file path.

    Raises:
        ValueError:
            If the file exceeds the maximum size.
    """

    file_path = Path(path)

    if file_path.stat().st_size > max_size_bytes:
        raise ValueError(f"File exceeds {max_size_bytes} bytes.")

    return file_path


def validate_non_empty_file(path: str | Path) -> Path:
    """
    Validate that a file is not empty.

    Args:
        path: File path.

    Returns:
        Validated file path.

    Raises:
        ValueError:
            If the file is empty.
    """

    file_path = Path(path)

    if file_path.stat().st_size == 0:
        raise ValueError("File is empty.")

    return file_path
