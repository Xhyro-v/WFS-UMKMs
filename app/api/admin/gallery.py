from fastapi import  APIRouter,HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session


from app.dependencies.auth import get_current_admin
from app.db.session import get_db
from app.schemas.gallery import GalleryResponse,GalleryCreate,GalleryUpdate
from app.services.gallery_service import (
    create_gallery_service,
    update_gallery_service,
    delete_gallery_service,
    get_all,
    get_by_id_service,
    get_published_gallery,
    get_un_published_gallery,
    publish_gallery_service,
    un_publish_gallery_service,
)


router = APIRouter(
      prefix="/admin/gallery",
      tags=["Admin Gallery"]
)


@router.post("/create")
def create_gallery(
      data: GalleryCreate,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return create_gallery_service(
            data,
            db,
            current_admin
      )



@router.get("/all")
def show_all_gallery(
      db: Session = Depends(get_db)
):
      return get_all(db)

@router.get("/{gallery_id}")
def show_gallery_by_id(
      gallery_id: int,
      db: Session = Depends(get_db)
):
      return get_by_id_service(db, gallery_id)

@router.get("/published-gallery")
def show_published_gallery(
      db: Session = Depends(get_db)
):
      return get_published_gallery(db)