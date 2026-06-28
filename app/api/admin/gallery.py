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

@router.put("/update/{gallery_id}")
def update_gallery(
      data: GalleryUpdate,
      gallery_id :int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return update_gallery_service(
              db,
              gallery_id,
              data
      )

@router.delete("/delete/{gallery_id}")
def delete_gallery(
      gallery_id: int,
      db : Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return delete_gallery_service(
            db,
            gallery_id
      )

@router.patch("/publish-gallery/{gallery_id}")
def publish_gallery(
      gallery_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return publish_gallery_service(
            db,
            gallery_id
      )

@router.patch("/unpublish-gallery/{gallery_id}")
def un_publish_gallery(
      gallery_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return un_publish_gallery_service(
            db,
            gallery_id
      )

@router.get("/galleries")
def show_all_gallery(
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return get_all(db)

@router.get("/published-gallery")
def show_published_gallery(
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return get_published_gallery(db)


@router.get("/unpublished-gallery")
def show_un_published_gallery(
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return get_un_published_gallery(db)

@router.get("/{gallery_id}")
def show_gallery_by_id(
      gallery_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return get_by_id_service(db, gallery_id)
