"""Pomelo tap class."""

from __future__ import annotations

from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_pomelo import streams


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
        th.Property(
            "start_date",
            th.DateTimeType,
            description="Earliest datetime to get data from",
        ),
    ).to_dict()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Pomelo streams.
        """
        return [
            streams.Users(tap=self),
            streams.Cards(tap=self),
            streams.Companies(tap=self),
        ]
