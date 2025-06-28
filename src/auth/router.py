from fastapi import APIRouter

from src.auth.config import authentication_backend, fastapi_users
from src.auth.schemas import UserCreate, UserRead, UserUpdate
from src.config import settings

auth_router = APIRouter(prefix=settings.api_prefix.v1.auth, tags=["Auth"])
users_router = APIRouter(prefix=settings.api_prefix.v1.users, tags=["Users"])

# /login
# /logout
auth_router.include_router(
    fastapi_users.get_auth_router(
        authentication_backend,
        requires_verification=True,
    )
)

# register
auth_router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))

# request-verify-token
# verify
auth_router.include_router(fastapi_users.get_verify_router(UserRead))

# /forgot-password
# /reset-password
auth_router.include_router(fastapi_users.get_reset_password_router())

# /me
# /{id}
users_router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate))
