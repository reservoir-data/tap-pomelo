"""Stream type classes for tap-pomelo."""

from __future__ import annotations

from singer_sdk import typing as th

from tap_pomelo.client import PomeloStream


LEGAL_ADDRESS = th.ObjectType(
    th.Property(
        "street_name",
        th.StringType,
    ),
    th.Property(
        "street_number",
        th.StringType,
    ),
    th.Property(
        "floor",
        th.StringType,
    ),
    th.Property(
        "apartment",
        th.StringType,
    ),
    th.Property(
        "zip_code",
        th.StringType,
    ),
    th.Property(
        "neighborhood",
        th.StringType,
    ),
    th.Property(
        "city",
        th.StringType,
    ),
    th.Property(
        "region",
        th.StringType,
    ),
    th.Property(
        "additional_info",
        th.StringType,
    ),
    th.Property(
        "country",
        th.StringType,  # ISO 3166 alpha-3
    ),
)


class Users(PomeloStream):
    """Users stream."""

    name = "users"
    path = "/users/v1"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The user's system ID",
        ),
        th.Property(
            "client_id",
            th.StringType,
        ),
        th.Property(
            "name",
            th.StringType,
            description="User's name",
        ),
        th.Property(
            "email",
            th.StringType,
            description="The user's email address",
        ),
        th.Property(
            "surname",
            th.StringType,
            description="User's surname",
        ),
        th.Property(
            "identification_type",
            th.StringType,
            description="User's identification document type",
        ),
        th.Property(
            "identification_value",
            th.StringType,
            description="User's identification document number",
        ),
        th.Property(
            "tax_identification_type",
            th.StringType,
            description="User's tax identification document type",
        ),
        th.Property(
            "tax_identification_value",
            th.StringType,
            description="User's tax identification document number",
        ),
        th.Property(
            "birthdate",
            th.DateType,
            description="User's birthdate",
        ),
        th.Property(
            "gender",
            th.DateType,
            description="User's gender",
            # pattern="^[A-Za-z\u00C0-\u00ff ]+$",
        ),
        th.Property(
            "phone",
            th.StringType,
            description="User's phone number",
        ),
        th.Property(
            "status",
            th.StringType,
            allowed_values=["ACTIVE", "BLOCKED"],
        ),
        th.Property(
            "operation_country",
            th.StringType,  # ISO 3166 alpha-3
            description="User's country of operation",
        ),
        th.Property(
            "legal_address",
            LEGAL_ADDRESS,
            description="User's legal address",
        ),
        th.Property(
            "nationality",
            th.StringType,  # ISO 3166 alpha-3
        ),
        # 'client_id',
    ).to_dict()


class Companies(PomeloStream):
    """Companies stream."""

    name = "companies"
    path = "/companies/v1"
    primary_keys = ["id"]
    replication_key = None

    schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The company's system ID",
        ),
        th.Property(
            "legal_name",
            th.StringType,
            description="Company's legal name",
        ),
        th.Property(
            "trade_name",
            th.StringType,
            description="Company's trade name",
        ),
        th.Property(
            "tax_identification_type",
            th.StringType,
            description="Company's tax identification document type",
        ),
        th.Property(
            "tax_identification_value",
            th.StringType,
            description="Company's tax identification document number",
        ),
        th.Property(
            "email",
            th.StringType,
            description="Company's email address",
        ),
        th.Property(
            "phone",
            th.StringType,
            description="Company's phone number",
        ),
        th.Property(
            "operation_country",
            th.StringType,  # ISO 3166 alpha-3
            description="Company's country of operation",
        ),
        th.Property(
            "type",
            th.StringType,
            description="Company type",
        ),
        th.Property(
            "status",
            th.StringType,
            allowed_values=["ACTIVE", "BLOCKED"],
        ),
        th.Property(
            "legal_address",
            LEGAL_ADDRESS,
            description="Company's legal address",
        ),
    ).to_dict()
