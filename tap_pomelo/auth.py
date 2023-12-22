"""Pomelo Authentication."""

from __future__ import annotations

from singer_sdk.authenticators import OAuthAuthenticator, SingletonMeta


class PomeloAuthenticator(OAuthAuthenticator, metaclass=SingletonMeta):
    """Authenticator class for Pomelo."""

    @property
    def oauth_request_body(self) -> dict:
        """Define the OAuth request body for the Pomelo API.

        Returns:
            Dictionary with request body for OAuth endpoint.
        """
        return {
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
            "audience": self.config["audience"],
            "grant_type": "client_credentials",
        }
