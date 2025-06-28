from typing import TYPE_CHECKING, Annotated

from fastapi import Depends

from src.auth.models import AccessToken, User
from src.datebase import db_helper

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


async def get_user_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):
    yield User.get_db(session=session)


async def get_access_token_db(
    session: Annotated["AsyncSession", Depends(db_helper.session_getter)],
):
    yield AccessToken.get_db(session=session)
