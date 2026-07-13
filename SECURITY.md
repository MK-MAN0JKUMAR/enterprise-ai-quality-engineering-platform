# Security Policy

Thank you for helping improve the security of the Enterprise AI Testing Platform.

Security is a core engineering principle of this project. Responsible disclosure helps protect users, contributors, and future deployments.

---

# Supported Versions

The project is under active development.

| Version    | Supported |
| ---------- | --------- |
| Unreleased |    Done   |
| 0.1.x      |    Done   |

As the project matures, this table will be updated to reflect supported release branches.

---

# Reporting a Security Vulnerability

If you discover a security vulnerability, please **do not** create a public GitHub issue.

Instead:

1. Contact the project maintainer privately.
2. Include a detailed description of the issue.
3. Provide reproduction steps if possible.
4. Include the affected version or commit.
5. Describe the potential impact.

A response will be provided as soon as practical.

---

# What to Include

When reporting a vulnerability, include:

* Description of the issue
* Steps to reproduce
* Expected behavior
* Actual behavior
* Impact assessment
* Environment information
* Screenshots or logs if applicable

Providing clear reproduction steps helps verify and resolve issues more efficiently.

---

# Disclosure Process

The general process for handling security issues is:

1. Receive the report.
2. Verify the vulnerability.
3. Assess severity and impact.
4. Develop and test a fix.
5. Release the fix.
6. Publish an advisory when appropriate.

---

# Security Goals

As the platform evolves, security considerations will include:

* Secure configuration management
* Secret handling
* Dependency management
* Supply chain security
* Secure plugin architecture
* Authentication and authorization
* Prompt injection testing
* AI security evaluation
* Dataset validation
* Secure CI/CD pipelines

---

# Dependency Management

Project dependencies should:

* Come from trusted sources.
* Be updated regularly.
* Be reviewed before introduction.
* Be removed when no longer required.

New dependencies should be evaluated for:

* Maintenance activity
* Community adoption
* License compatibility
* Security history
* Long-term sustainability

---

# Supported Development Practices

Contributors are expected to:

* Run the local quality gate before submitting changes.
* Keep dependencies current.
* Avoid committing secrets, credentials, or API keys.
* Follow the project's coding and documentation standards.

---

# Security Scope

Security-related improvements may include:

* Dependency updates
* Configuration hardening
* Secret management
* Vulnerability remediation
* Security testing
* Secure defaults

These changes should be submitted through dedicated feature or security-focused branches whenever practical.

---

# Future Enhancements

As the platform matures, the security program may expand to include:

* Automated dependency scanning
* Static Application Security Testing (SAST)
* Secret scanning
* Software Bill of Materials (SBOM)
* Container image scanning
* Supply chain verification
* Security advisories
* CVE tracking
* AI-specific security testing

---

Thank you for helping maintain a secure and reliable engineering platform.
