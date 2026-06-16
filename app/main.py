from app.core.config import SECRET_KEY, DEBUG
from fastapi import FastAPI
from app.api.login import router as admin_router

app = FastAPI()

app.include_router(admin_router)