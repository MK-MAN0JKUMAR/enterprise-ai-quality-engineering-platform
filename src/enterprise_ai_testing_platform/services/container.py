"""
Service container.
"""

from .registry import ServiceRegistry


class ServiceContainer:
    """
    High-level service container.

    Wraps a service registry and exposes a simple API
    for future dependency resolution.
    """

    def __init__(self) -> None:
        """Initialize the container."""

        self._registry = ServiceRegistry()

    @property
    def registry(self) -> ServiceRegistry:
        """
        Return the underlying registry.
        """

        return self._registry

    def register(
        self,
        name: str,
        service: object,
    ) -> None:
        """
        Register a service.
        """

        self._registry.register(name, service)

    def unregister(self, name: str) -> None:
        """
        Remove a registered service.
        """

        self._registry.unregister(name)

    def resolve(self, name: str) -> object:
        """
        Resolve a service.

        Raises:
            KeyError:
                If the service is not registered.
        """

        return self._registry.get(name)

    def contains(self, name: str) -> bool:
        """
        Check whether a service exists.
        """

        return self._registry.contains(name)

    def clear(self) -> None:
        """
        Remove all services.
        """

        self._registry.clear()
