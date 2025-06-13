from fastapi import FastAPI

from api import router as api_router
from config import settings

app = FastAPI()
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"Hello": f"World!{settings.access_token.lifetime_seconds}"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", reload=True)
