from fastapi import APIRouter

from auth.config import authentication_backend, fastapi_users
from auth.schemas import UserCreate, UserRead
from config import settings

router = APIRouter(prefix=settings.api_prefix.v1.auth, tags=["Auth"])

# /login
# /logout
router.include_router(fastapi_users.get_auth_router(authentication_backend))

# register
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate))
