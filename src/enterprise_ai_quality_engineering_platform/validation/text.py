"""
Text validation utilities.
"""

import re

_IDENTIFIER_PATTERN = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


def validate_not_blank(value: str) -> str:
    """
    Validate that a string is not blank.
    """

    if not value.strip():
        raise ValueError("Value cannot be blank.")

    return value


def validate_min_length(value: str, minimum: int) -> str:
    """
    Validate minimum length.
    """

    if len(value) < minimum:
        raise ValueError(f"Value must contain at least {minimum} characters.")

    return value


def validate_max_length(value: str, maximum: int) -> str:
    """
    Validate maximum length.
    """

    if len(value) > maximum:
        raise ValueError(f"Value must contain at most {maximum} characters.")

    return value


def validate_identifier(value: str) -> str:
    """
    Validate an identifier.
    """

    if not _IDENTIFIER_PATTERN.fullmatch(value):
        raise ValueError(f"Invalid identifier: {value}")

    return value
