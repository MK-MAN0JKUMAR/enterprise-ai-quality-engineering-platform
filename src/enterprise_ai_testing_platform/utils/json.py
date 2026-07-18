"""
JSON utility functions.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast


def read_json_file(path: Path | str) -> dict[str, Any]:
    """
    Read a JSON file.

    Args:
        path:
            Path to the JSON file.

    Returns:
        Parsed JSON object.

    Raises:
        FileNotFoundError:
            If the file does not exist.

        json.JSONDecodeError:
            If the file contains invalid JSON.

        TypeError:
            If the JSON root is not an object.
    """

    with Path(path).open(encoding="utf-8") as file:
        data = cast(dict[str, Any], json.load(file))

    return data


def write_json_file(
    path: Path | str,
    data: dict[str, Any],
) -> None:
    """
    Write a JSON object to a file.

    Parent directories are created automatically.

    Args:
        path:
            Destination file.

        data:
            JSON object to write.
    """

    file_path = Path(path)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open("w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            indent=4,
            sort_keys=True,
            ensure_ascii=False,
        )
