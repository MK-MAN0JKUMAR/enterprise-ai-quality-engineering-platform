# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Added

#### Provider Configuration

- Introduced a configuration-driven provider architecture.
- Added `ProviderSettings` as the central provider configuration model.
- Added `ProviderConfig` base configuration model.
- Added provider default configuration constants.
- Added provider type configuration models.
- Added support for Groq provider configuration.
- Added support for Ollama provider configuration.
- Added support for Groq provider configuration.
- Added centralized provider selection through `ProviderFactory` and `ProviderRegistry`.
- Added constructor-based dependency injection for providers.

#### Testing

- Added comprehensive unit tests for provider configuration.
- Added ProviderFactory unit tests.
- Added comprehensive unit tests for Gemini provider.
- Increased overall test coverage to **95.48%**.
- Total automated tests increased to **119**.

#### Documentation

- Added Provider Configuration documentation.
- Added ADR-0004 documenting the Provider Configuration Architecture.

### Changed

#### Provider Architecture

- Providers no longer manage configuration directly.
- Provider creation is centralized in `ProviderFactory`.
- Runtime providers now receive configuration through constructor injection.
- Improved separation between configuration and runtime implementation.

#### Quality

- Ruff ✔ Passed
- Black ✔ Passed
- MyPy ✔ Passed
- Pytest ✔ Passed
- Pre-commit ✔ Passed

---

## [0.1.0] - Initial Bootstrap

### Added

#### Repository Foundation

- Initialized Git repository.
- Created GitHub repository.
- Established enterprise project structure.
- Added enterprise `.gitignore`.
- Standardized empty directory strategy using `.gitkeep`.

#### Architecture

- Defined project vision and engineering philosophy.
- Designed modular enterprise architecture.
- Established provider abstraction strategy.
- Defined plugin architecture.
- Created long-term implementation roadmap.

#### Python Project

- Created `pyproject.toml`.
- Standardized on Python 3.12.
- Adopted `uv` for dependency and environment management.
- Configured modern Python packaging.

#### Development Environment

- Configured virtual environment workflow.
- Added Ruff.
- Added Black.
- Added MyPy.
- Added Pytest.
- Added Coverage.
- Added pre-commit.

#### Continuous Integration

- Added GitHub Actions quality workflow.

#### Testing

- Added initial package verification test.
- Established automated testing foundation.

#### Documentation

- Added project README.
- Added development setup guide.
- Added development command reference.
- Added contribution guidelines.
- Initialized changelog.

---

## Versioning Policy

This project follows Semantic Versioning (SemVer).

- **MAJOR** – Breaking architectural or API changes.
- **MINOR** – New backward-compatible functionality.
- **PATCH** – Backward-compatible bug fixes, documentation improvements, and maintenance updates.

---

## Release Strategy

Every release should:

- Pass all quality gates.
- Pass all automated tests.
- Update documentation when required.
- Update this changelog before release.
- Be tagged in Git using Semantic Versioning.
