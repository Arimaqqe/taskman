from fastapi import APIRouter

from auth.config import authentication_backend, fastapi_users
from auth.schemas import UserCreate, UserRead, UserUpdate
from config import settings

auth_router = APIRouter(prefix=settings.api_prefix.v1.auth, tags=["Auth"])
users_router = APIRouter(prefix=settings.api_prefix.v1.users, tags=["Users"])

# /login
# /logout
auth_router.include_router(fastapi_users.get_auth_router(authentication_backend))

# register
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

# /me
# /{id}
users_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
