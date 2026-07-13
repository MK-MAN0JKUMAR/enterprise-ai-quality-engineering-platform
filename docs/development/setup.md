# Development Setup

This guide explains how to set up a local development environment for the Enterprise AI Testing Platform.

This is a one-time setup guide for new contributors.

For daily development commands and workflows, refer to:

* `docs/development/commands.md`

---

# Prerequisites

Install the following software before cloning the repository.

* Git
* Python 3.12
* uv
* GitHub account

---

# Clone the Repository

```bash
git clone <repository-url>
cd enterprise-ai-testing-platform
```

---

# Verify Python Installation

The project is standardized on Python 3.12.

Verify your installed versions:

```bash
py --list
```

Verify the active interpreter:

```bash
python --version
```

---

# Install uv

If `uv` is not already installed:

### Windows

```powershell
winget install --id=astral-sh.uv -e
```

Verify the installation:

```bash
uv --version
```

---

# Pin the Python Version

Pin the project to Python 3.12.

```bash
uv python pin 3.12
```

This creates a `.python-version` file to ensure that local development and CI use the same Python version.

---

# Create the Virtual Environment

Create the project's virtual environment.

```bash
uv venv
```

---

# Install Project Dependencies

Install all project dependencies.

```bash
uv sync
```

---

# Install Git Hooks

Install the project's pre-commit hooks.

```bash
uv run pre-commit install
```

---

# Verify the Setup

Confirm the correct Python interpreter is being used.

```bash
uv run python --version
```

The output should display Python 3.12.x.

---

# Project Structure

The repository follows a modular architecture.

```text
enterprise-ai-testing-platform/
├── app/
├── assets/
├── configs/
├── docs/
├── examples/
├── scripts/
├── src/
├── tests/
├── .github/
├── pyproject.toml
└── README.md
```

---

# Branch Strategy

Development must never occur directly on the `main` branch.

Create a dedicated branch for every change.

Examples:

```text
feature/project-bootstrap
feature/provider-abstraction
feature/evaluation-engine
bugfix/config-loading
hotfix/version-0.2.1
release/v0.2.0
```

---

# Development Standards

Every contribution should:

* Pass the local quality gate before being committed.
* Include automated tests when production code is added or modified.
* Update documentation when behavior changes.
* Preserve backward compatibility unless an approved breaking change is planned.
* Follow the established architecture and coding standards.

---

# Next Steps

Your local development environment is now ready.

For all day-to-day development activities, use the documentation in:

* `docs/development/commands.md`

This document is the single source of truth for:

* Development commands
* Code formatting
* Linting
* Type checking
* Testing
* Pre-commit hooks
* Local quality gate
* Dependency management
* Daily development workflow
