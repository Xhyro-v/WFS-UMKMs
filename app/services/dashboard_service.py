from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.repositories.dashboard_admin_repository import (
    get_menu_summary
)


def get_dashboard_summary(db: Session):
    menu = get_menu_summary(db)
    # content = content_repository.get_content_summary(db)
#     gallery = gallery_repository.get_gallery_summary(db)

    return {
        "menu": menu,
#         "content": content,
#         "gallery": gallery,
    }