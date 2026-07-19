"""
URL validation utilities.
"""

from urllib.parse import urlparse


def validate_http_url(url: str) -> str:
    """
    Validate an HTTP or HTTPS URL.
    """

    parsed = urlparse(url)

    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"Invalid URL: {url}")

    return url


def validate_https_url(url: str) -> str:
    """
    Validate an HTTPS URL.
    """

    parsed = urlparse(url)

    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError(f"Invalid HTTPS URL: {url}")

    return url
