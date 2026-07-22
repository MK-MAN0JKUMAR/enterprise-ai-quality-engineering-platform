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
- Added support for Gemini provider configuration.
- Added support for LM Studio provider configuration.
- Added provider-specific configuration for local and cloud LLM providers.
- Added centralized runtime provider selection through PlatformSettings.
- Added centralized provider selection through `ProviderFactory` and `ProviderRegistry`.
- Added runtime registration for Gemini provider.
- Added runtime registration for LM Studio provider.
- Added constructor-based dependency injection for providers.
- Added Gemini runtime provider implementation.
- Added LM Studio runtime provider implementation.
- Added provider metadata support for runtime providers.
- Added provider lifecycle implementation (initialize/shutdown).
- Added LM Studio runtime provider implementation.
- Added LM Studio provider constants.
- Added LM Studio provider registration in ProviderRegistry.
- Added LM Studio provider creation through ProviderFactory.

#### Testing

- Added comprehensive unit tests for provider configuration.
- Added ProviderFactory unit tests.
- Added ProviderRegistry unit tests.
- Added LM Studio provider unit tests.
- Added LM Studio configuration unit tests.
- Added comprehensive unit tests for Gemini provider.
- Added comprehensive unit tests for LM Studio provider.
- Increased overall test coverage to **95.77%**.
- Total automated tests increased to **128**.

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
