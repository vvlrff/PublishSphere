from urllib.parse import urlunsplit

from shared import settings


def get_pg_uri(
    username=settings.PG_USERNAME,
    password=settings.PG_PASSWORD,
    host=settings.PG_HOST,
    port=settings.PG_PORT,
    db=settings.PG_DB,
    protocol=settings.PG_PROTOCOL,
    uri_query=settings.PG_URI_QUERY,
):
    return urlunsplit(
        (protocol, f"{username}:{password}@{host}:{port}", db, uri_query, str())
    )


# def get_pg_uri_for_ads(
#     username=settings.PG_ADS_USERNAME,
#     password=settings.PG_ADS_PASSWORD,
#     host=settings.PG_ADS_HOST,
#     port=settings.PG_ADS_PORT,
#     db=settings.PG_ADS_DB,
#     protocol=settings.PG_PROTOCOL,
#     uri_query=settings.PG_URI_QUERY,
# ):
#     return urlunsplit(
#         (protocol, f"{username}:{password}@{host}:{port}", db, uri_query, str())
#     )
