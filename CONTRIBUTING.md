# Contributing

Thank you for your interest in contributing to the Enterprise AI Testing Platform.

This project is designed as a long-term, production-quality engineering platform focused on AI quality engineering, software architecture, and enterprise development practices.

All contributions should align with the project's architecture, engineering standards, and long-term vision.

---

# Development Philosophy

The project prioritizes:

* Maintainability over rapid feature development
* Clean Architecture
* Modular design
* Provider independence
* Strong typing
* Automated testing
* Documentation-first development
* Backward compatibility whenever practical

Every change should improve the project without introducing unnecessary complexity.

---

# Before You Start

Before making changes:

1. Read the project documentation.
2. Understand the current architecture.
3. Create a dedicated feature branch.
4. Keep changes focused on a single objective.
5. Avoid unrelated refactoring.

---

# Branch Strategy

Never develop directly on the `main` branch.

Examples:

```text
feature/project-bootstrap
feature/provider-abstraction
feature/evaluation-engine
bugfix/config-loading
hotfix/version-0.2.1
release/v0.2.0
```

Each branch should address one well-defined objective.

---

# Development Environment

Follow the setup guide:

* `docs/development/setup.md`

Daily development commands are documented in:

* `docs/development/commands.md`

---

# Coding Standards

All production code should:

* Follow the project's architecture.
* Include type hints.
* Follow Black formatting.
* Pass Ruff linting.
* Pass MyPy type checking.
* Keep functions and classes focused on a single responsibility.
* Avoid duplicate logic.
* Avoid unnecessary abstractions.
* Favor composition over inheritance where appropriate.

---

# Testing Requirements

Production code changes should include automated tests whenever applicable.

The project currently uses:

* Pytest
* Coverage

Future phases will introduce additional testing for:

* Integration
* Performance
* AI Evaluation
* End-to-End
* Security

---

# Local Quality Gate

Before committing code, verify the local quality gate passes.

```bash
uv run ruff check .
uv run black --check .
uv run python -m mypy src
uv run pytest
```

Run the pre-commit hooks before creating a commit.

```bash
uv run pre-commit run --all-files
```

---

# Documentation

Documentation is part of the codebase.

Update documentation whenever:

* behavior changes
* configuration changes
* public interfaces change
* new features are introduced

---

# Pull Requests

Every Pull Request should:

* Focus on a single objective.
* Include a clear description.
* Pass all quality checks.
* Include tests when production code changes.
* Update documentation when required.
* Preserve backward compatibility unless an approved breaking change is planned.

---

# Reporting Issues

When reporting bugs or requesting features, use the GitHub issue templates provided in the repository.

---

# Architecture

Do not introduce new architectural layers or abstractions without a clear justification.

When proposing architectural changes:

* Explain the problem.
* Describe the proposed solution.
* Evaluate alternatives.
* Consider long-term maintenance.
* Assess the impact on existing modules.

Major architectural changes should be implemented in dedicated architecture-focused branches rather than feature branches.

---

# Code of Conduct

By participating in this project, you agree to follow the guidelines described in `CODE_OF_CONDUCT.md`.

---

Thank you for helping maintain a high-quality engineering project.
