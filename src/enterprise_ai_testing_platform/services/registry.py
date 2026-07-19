"""
Service registry implementation.
"""

from collections.abc import Iterator


class ServiceRegistry:
    """
    Registry for named services.
    """

    def __init__(self) -> None:
        """Initialize an empty registry."""

        self._services: dict[str, object] = {}

    def register(
        self,
        name: str,
        service: object,
    ) -> None:
        """
        Register a service.

        Raises:
            ValueError:
                If the service already exists.
        """

        if name in self._services:
            raise ValueError(f"Service '{name}' is already registered.")

        self._services[name] = service

    def unregister(self, name: str) -> None:
        """
        Remove a registered service.
        """

        self._services.pop(name, None)

    def get(self, name: str) -> object:
        """
        Retrieve a registered service.

        Raises:
            KeyError:
                If the service does not exist.
        """

        try:
            return self._services[name]
        except KeyError as error:
            raise KeyError(f"Unknown service '{name}'.") from error

    def contains(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return name in self._services

    def clear(self) -> None:
        """
        Remove all registered services.
        """

        self._services.clear()

    def names(self) -> list[str]:
        """
        Return registered service names.
        """

        return sorted(self._services.keys())

    def __len__(self) -> int:
        """
        Return number of registered services.
        """

        return len(self._services)

    def __iter__(self) -> Iterator[str]:
        """
        Iterate over service names.
        """

        return iter(self.names())
