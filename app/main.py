from fastapi import FastAPI

from app.core.config import SECRET_KEY, DEBUG
from app.api.auth import router as auth_router

app = FastAPI(
    title="WFS UMKM API"
)

app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "WFS API is running!"
    }
