"""Pomelo tap class."""

from __future__ import annotations

import sys

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_pomelo import streams

if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override


class TapPomelo(Tap):
    """Singer tap for Pomelo."""

    name = "tap-pomelo"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "client_id",
            th.StringType,
            required=True,
            secret=True,
            description="Client ID to authenticate in Pomelo",
        ),
        th.Property(
            "client_secret",
            th.StringType,
            required=True,
            secret=True,
            description="Client secret to authenticate in Pomelo",
        ),
        th.Property(
            "audience",
            th.StringType,
            required=True,
            description="Audience to authenticate in Pomelo",
            default="https://auth.pomelo.la",
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=True,
            description="Base URL for the API",
            default="https://api.pomelo.la",
        ),
    ).to_dict()

    @override
    def discover_streams(self) -> list[Stream]:
        return [
            streams.Users(tap=self),
            streams.Cards(tap=self),
            streams.Companies(tap=self),
        ]
