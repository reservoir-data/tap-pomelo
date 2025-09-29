"""REST client handling, including PomeloStream base class."""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

from singer_sdk import RESTStream
from singer_sdk.pagination import BasePageNumberPaginator

from tap_pomelo.auth import PomeloAuthenticator

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override

if TYPE_CHECKING:
    from singer_sdk.helpers.types import Context


class PomeloStream(RESTStream[int]):
    """Pomelo stream class."""

    records_jsonpath = "$.data[*]"

    @property
    @override
    def url_base(self) -> str:
        return self.config["api_url"]  # type: ignore[no-any-return]

    @property
    @override
    def authenticator(self) -> PomeloAuthenticator:
        return PomeloAuthenticator(
            client_id=self.config["client_id"],
            client_secret=self.config["client_secret"],
            audience=self.config["audience"],
            auth_endpoint=self.config["api_url"] + "/oauth/token",
        )

    @override
    def get_new_paginator(self) -> BasePageNumberPaginator:
        return BasePageNumberPaginator(start_value=0)

    @override
    def get_url_params(
        self,
        context: Context | None,
        next_page_token: int | None,
    ) -> dict[str, Any]:
        return {
            "page[number]": next_page_token or 0,
            "page[size]": 500,
        }
