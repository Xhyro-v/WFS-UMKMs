from fastapi import  APIRouter,HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.content import Content
from app.schemas.content import ContentResponse
from app.enums.content_type import ContentType
from app.services.content_service import (
      get_by_id_published_service,
      get_all_published_content,
      get_by_published_type
)


router = APIRouter(
      prefix="/content",
      tags=["Content"]
)

@router.get("/contents")
def show_all_published_content(
      db: Session = Depends(get_db)
):
      return get_all_published_content(db)

@router.get("/{content_type}")
def show_by_published_type_content(
      content_type: ContentType,
      db: Session = Depends(get_db)
):
      return get_by_published_type(db,content_type)

@router.get("{content_id}")
def show_by_id_published(
      content_id: int,
      db: Session = Depends(get_db)
):
      return get_by_id_published_service(db,content_id)
