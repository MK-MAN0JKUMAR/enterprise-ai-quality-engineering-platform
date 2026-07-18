"""
Tests for hashing utilities.
"""

from enterprise_ai_testing_platform.utils import md5_hash, sha256_hash


def test_md5_hash_returns_expected_value() -> None:
    """Verify MD5 hashing."""

    assert md5_hash("hello") == "5d41402abc4b2a76b9719d911017c592"


def test_sha256_hash_returns_expected_value() -> None:
    """Verify SHA-256 hashing."""

    assert (
        sha256_hash("hello") == "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
    )
