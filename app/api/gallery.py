from fastapi import  APIRouter,HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.gallery import GalleryResponse
from app.services.gallery_service import (
    get_all,
    get_by_id_service,
    get_published_gallery,
    get_gallery_published_id_service
)


router = APIRouter(
      prefix="/gallery",
      tags=["Gallery"]
)


@router.get("/galleries")
def show_published_gallery(
      db: Session = Depends(get_db)
):
      return get_published_gallery(db)

@router.get("/{gallery_id}")
def show_published_gallery_by_id(
      gallery_id: int,
      db: Session = Depends(get_db)
):
      return get_gallery_published_id_service(db,gallery_id)