from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import OperationalError

from app.core.config import SECRET_KEY, DEBUG
from app.api.auth import router as auth_router
from app.api.menu import router as menu_router
from app.errors.error_handler import database_error_handler,validation_error_handler


app = FastAPI(
    title="WFS UMKM API"
)

app.add_exception_handler(
    OperationalError,
    database_error_handler,
)

app.add_exception_handler(
    RequestValidationError,
    validation_error_handler
)

app.include_router(auth_router)
app.include_router(menu_router)


@app.get("/")
def root():
    return {
        "message": "WFS API is running!"
    }
