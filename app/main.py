from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from sqlalchemy.exc import OperationalError

from app.core.config import SECRET_KEY, DEBUG
from app.api.auth import router as auth_router
from app.api.menu import router as menu_router
from app.api.gallery import router as gallery_router
from app.api.content import router as content_router
from app.api.admin.gallery import router as admin_gallery_router
from app.api.admin.content import router as admin_content_router
from app.errors.error_handler import database_error_handler,validation_error_handler
from app.dependencies.auth import get_current_admin


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
app.include_router(gallery_router)
app.include_router(content_router)


app.include_router(admin_gallery_router)
app.include_router(admin_content_router)


@app.get("/")
def root():
    return {
        "message": "WFS API is running!"
    }
