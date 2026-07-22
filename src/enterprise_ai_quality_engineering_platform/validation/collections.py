"""
Collection validation utilities.
"""

from collections.abc import Collection


def validate_not_empty[T](values: Collection[T]) -> Collection[T]:
    """
    Validate that a collection is not empty.

    Args:
        values: Collection to validate.

    Returns:
        Validated collection.

    Raises:
        ValueError:
            If the collection is empty.
    """

    if not values:
        raise ValueError("Collection cannot be empty.")

    return values


def validate_length[T](
    values: Collection[T],
    *,
    minimum: int = 0,
    maximum: int | None = None,
) -> Collection[T]:
    """
    Validate collection length.

    Args:
        values: Collection to validate.
        minimum: Minimum allowed size.
        maximum: Maximum allowed size.

    Returns:
        Validated collection.

    Raises:
        ValueError:
            If the collection length is outside the allowed range.
    """

    size = len(values)

    if size < minimum:
        raise ValueError(f"Collection must contain at least {minimum} items.")

    if maximum is not None and size > maximum:
        raise ValueError(f"Collection must contain at most {maximum} items.")

    return values


def validate_unique[T](values: Collection[T]) -> Collection[T]:
    """
    Validate that a collection contains unique values.

    Args:
        values: Collection to validate.

    Returns:
        Validated collection.

    Raises:
        ValueError:
            If duplicate values are found.
    """

    if len(values) != len(set(values)):
        raise ValueError("Collection contains duplicate values.")

    return values
