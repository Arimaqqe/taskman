from fastapi import APIRouter

from auth.router import auth_router, users_router
from config import settings

router = APIRouter(prefix=settings.api_prefix.v1.prefix)

router.include_router(auth_router)
router.include_router(users_router)
