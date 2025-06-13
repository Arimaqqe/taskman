from typing import TYPE_CHECKING, Annotated

from fastapi import Depends
from fastapi_users.authentication import AuthenticationBackend, BearerTransport
from fastapi_users.authentication.strategy.db import DatabaseStrategy

from src.auth.utils import get_access_token_db
from src.config import settings

if TYPE_CHECKING:
    from fastapi_users.authentication.strategy.db import AccessTokenDatabase

    from src.auth.models import AccessToken

bearer_transport = BearerTransport(
    # TODO: update url
    tokenUrl="auth/jwt/login"
)


def get_database_strategy(
    access_token_db: Annotated[
        "AccessTokenDatabase[AccessToken]", Depends(get_access_token_db)
    ],
):
    return DatabaseStrategy(
        database=access_token_db,
        lifetime_seconds=settings.access_token.lifetime_seconds,
    )


authentication_backend = AuthenticationBackend(
    name="access-token-db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
