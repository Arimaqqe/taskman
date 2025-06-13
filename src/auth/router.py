from fastapi import APIRouter

from auth.config import authentication_backend, fastapi_users
from config import settings

router = APIRouter(prefix=settings.api_prefix.v1.auth, tags=["Auth"])

router.include_router(fastapi_users.get_auth_router(authentication_backend))
