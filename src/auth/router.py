from fastapi import APIRouter

from config import settings

router = APIRouter(prefix=settings.api_prefix.v1.auth, tags=["Auth"])


@router.get("/login")
def login():
    return {"message": "Login"}

