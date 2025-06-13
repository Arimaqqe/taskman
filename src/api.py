from fastapi import APIRouter

from auth.router import router as auth_router
from config import settings

router = APIRouter(prefix=settings.api_prefix.v1.prefix)

router.include_router(auth_router)
