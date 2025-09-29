"""Pomelo Authentication."""

from __future__ import annotations

from typing import Any

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


class PomeloAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Pomelo."""

    def __init__(self, *args: Any, audience: str, **kwargs: Any) -> None:
        """Initialize the Pomelo authenticator."""
        super().__init__(*args, **kwargs)
        self.audience = audience

    @property
    def oauth_request_body(self) -> dict[str, str]:
        """Define the OAuth request body for the Pomelo API.

        Returns:
            Dictionary with request body for OAuth endpoint.
        """
        return {
            "client_id": self.client_id,  # type: ignore[dict-item]
            "client_secret": self.client_secret,  # type: ignore[dict-item]
            "audience": self.audience,
            "grant_type": "client_credentials",
        }
