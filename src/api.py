from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer

from src.auth.router import auth_router, users_router
from src.config import settings

http_bearer = HTTPBearer(auto_error=False)

router = APIRouter(
    prefix=settings.api_prefix.v1.prefix,
    dependencies=[Depends(http_bearer)],
)

router.include_router(auth_router)
router.include_router(users_router)
