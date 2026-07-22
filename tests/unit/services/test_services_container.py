"""
Tests for the service container.
"""

import pytest

from enterprise_ai_quality_engineering_platform.services.container import (
    ServiceContainer,
)


def test_register_and_resolve_service() -> None:
    """Register and resolve a service."""

    container = ServiceContainer()

    service = object()

    container.register("service", service)

    assert container.resolve("service") is service


def test_contains_service() -> None:
    """Verify service existence."""

    container = ServiceContainer()

    container.register("service", object())

    assert container.contains("service")


def test_unregister_service() -> None:
    """Remove a registered service."""

    container = ServiceContainer()

    container.register("service", object())

    container.unregister("service")

    assert not container.contains("service")


def test_clear_container() -> None:
    """Remove all registered services."""

    container = ServiceContainer()

    container.register("a", object())
    container.register("b", object())

    container.clear()

    assert not container.contains("a")
    assert not container.contains("b")


def test_resolve_unknown_service() -> None:
    """Reject unknown service."""

    container = ServiceContainer()

    with pytest.raises(KeyError):
        container.resolve("missing")


def test_registry_property() -> None:
    """Expose the underlying registry."""

    container = ServiceContainer()

    assert container.registry is not None
