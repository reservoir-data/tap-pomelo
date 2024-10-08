"""REST client handling, including PomeloStream base class."""

from __future__ import annotations

from typing import Any

from singer_sdk import RESTStream

from tap_pomelo.auth import PomeloAuthenticator


class PomeloStream(RESTStream):
    """Pomelo stream class."""

    records_jsonpath = "$.data[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.next_page"  # noqa: S105

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings.

        Returns:
            The API URL root, configurable via tap settings.
        """
        return self.config["api_url"]

    @property
    def authenticator(self) -> PomeloAuthenticator:
        """Get an authenticator object.

        Returns:
            The authenticator instance for this REST stream.
        """
        return PomeloAuthenticator(
            self,
            auth_endpoint=self.config["api_url"] + "/oauth/token",
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed.

        Returns:
            A dictionary of HTTP headers.
        """
        headers = {}
        headers["User-Agent"] = f"{self.tap_name}/{self._tap.plugin_version}"
        return headers

    def get_url_params(
        self,
        context: dict | None,  # noqa: ARG002
        next_page_token: Any | None,  # noqa: ARG002, ANN401
    ) -> dict[str, Any]:
        """Get URL query parameters.

        Args:
            context: Stream sync context.
            next_page_token: Next offset.

        Returns:
            Mapping of URL query parameters.
        """
        params: dict = {}
        return params
