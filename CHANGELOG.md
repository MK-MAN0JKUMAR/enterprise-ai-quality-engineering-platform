# Changelog

All notable changes to this project will be documented in this file.

The format is based on **Keep a Changelog** and this project follows **Semantic Versioning (SemVer)**.

---

## [Unreleased]

### Planned

* Continue development of the Enterprise AI Testing Platform.
* Add new features through dedicated feature branches.
* Preserve backward compatibility whenever practical.

---

## [0.1.0] - Initial Bootstrap

### Added

#### Repository Foundation

* Initialized Git repository.
* Created GitHub repository.
* Established initial project structure.
* Added enterprise `.gitignore`.
* Standardized empty directory strategy using `.gitkeep`.

#### Architecture

* Defined project vision and engineering philosophy.
* Designed modular enterprise architecture.
* Established provider abstraction strategy.
* Defined plugin architecture.
* Created long-term implementation roadmap.

#### Python Project

* Created `pyproject.toml`.
* Standardized on Python 3.12.
* Adopted `uv` for package and environment management.
* Configured modern Python packaging.

#### Development Environment

* Configured virtual environment workflow.
* Added Ruff.
* Added Black.
* Added MyPy.
* Added Pytest.
* Added Coverage.
* Added pre-commit.

#### Continuous Integration

* Added GitHub Actions quality workflow.

#### Testing

* Added initial package verification test.
* Established automated testing foundation.

#### Documentation

* Added project README.
* Added development setup guide.
* Added development command reference.
* Added contribution guidelines.
* Initialized changelog.

---

## Versioning Policy

This project follows Semantic Versioning.

* **MAJOR** – Breaking architectural or API changes.
* **MINOR** – New backward-compatible functionality.
* **PATCH** – Backward-compatible fixes, documentation improvements, and maintenance updates.

---

## Release Strategy

Every release should:

* Pass all quality gates.
* Pass all automated tests.
* Update documentation when required.
* Update this changelog before release.
* Be tagged in Git using Semantic Versioning.
