import asyncio
import contextlib

from src.auth.manager import UserManager, get_user_db, get_user_manager
from src.auth.models import User
from src.auth.schemas import UserCreate
from src.config import settings
from src.datebase import db_helper

get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)

DEFAULT_EMAIL = settings.default_user.email
DEFAULT_PASSWORD = settings.default_user.password
DEFAULT_IS_ACTIVE = settings.default_user.is_active
DEFAULT_IS_SUPERUSER = settings.default_user.is_superuser
DEFAULT_IS_VERIFIED = settings.default_user.is_verified


async def create_user(user_manager: UserManager, user_create: UserCreate) -> User:
    user = await user_manager.create(user_create=user_create, safe=False)
    return user


async def create_superuser(
    email: str = DEFAULT_EMAIL,
    password: str = DEFAULT_PASSWORD,
    is_active: bool = DEFAULT_IS_ACTIVE,
    is_superuser: bool = DEFAULT_IS_SUPERUSER,
    is_verified: bool = DEFAULT_IS_VERIFIED,
):
    user_create = UserCreate(
        email=email,
        password=password,
        is_active=is_active,
        is_superuser=is_superuser,
        is_verified=is_verified,
    )
    async with db_helper.session_factory() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                return await create_user(
                    user_manager=user_manager,
                    user_create=user_create,
                )


if __name__ == "__main__":
    asyncio.run(create_superuser())
