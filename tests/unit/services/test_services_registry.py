"""
Tests for the service registry.
"""

import pytest

from enterprise_ai_quality_engineering_platform.services.registry import (
    ServiceRegistry,
)


def test_register_and_get_service() -> None:
    """Register and retrieve a service."""

    registry = ServiceRegistry()

    service = object()

    registry.register("service", service)

    assert registry.get("service") is service


def test_duplicate_registration_raises() -> None:
    """Reject duplicate service registration."""

    registry = ServiceRegistry()

    registry.register("service", object())

    with pytest.raises(ValueError):
        registry.register("service", object())


def test_unregister_service() -> None:
    """Remove a registered service."""

    registry = ServiceRegistry()

    registry.register("service", object())

    registry.unregister("service")

    assert not registry.contains("service")


def test_unknown_service_raises() -> None:
    """Reject unknown service lookup."""

    registry = ServiceRegistry()

    with pytest.raises(KeyError):
        registry.get("unknown")


def test_clear_registry() -> None:
    """Clear all services."""

    registry = ServiceRegistry()

    registry.register("a", object())
    registry.register("b", object())

    registry.clear()

    assert len(registry) == 0


def test_registry_names() -> None:
    """Return sorted service names."""

    registry = ServiceRegistry()

    registry.register("b", object())
    registry.register("a", object())

    assert registry.names() == ["a", "b"]


def test_registry_iteration() -> None:
    """Iterate over service names."""

    registry = ServiceRegistry()

    registry.register("alpha", object())
    registry.register("beta", object())

    assert list(registry) == ["alpha", "beta"]
