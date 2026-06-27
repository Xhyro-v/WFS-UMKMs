from fastapi import  APIRouter,HTTPException, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.dependencies.auth import get_current_admin
from app.models.content import Content
from app.schemas.content import ContentCreate, ContentUpdate, ContentResponse
from app.enums.content_type import ContentType
from app.services.content_service import create_content_service, update_content_service, delete_content_service, get_by_id_service, get_all_content, get_by_type_service, publish_content_service, un_publish_content_service, get_by_published, get_by_un_published


router = APIRouter(
      prefix="/content",
      tags=["Content"]
)

@router.post("/create")
def create_content(
      data : ContentCreate,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return create_content_service(
            db,
            data,
            current_admin
      )

@router.put("/update/{content_id}")
def update_content(
      data : ContentUpdate,
      content_id : int,
      db : Session = Depends(get_db),
      current_admin = Depends(get_current_admin)

):
      return update_content_service(
            db,
            content_id,
            data
      )

@router.delete("/delete/{content_id}")
def delete_content(
      content_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return delete_content_service(db, content_id)


@router.get("{content_id}")
def show_by_id(
      content_id: int,
      db: Session = Depends(get_db)
):
      return get_by_id_service(db,content_id)

@router.get("/all")
def show_all_content(
      db: Session = Depends(get_db)
):
      return get_all_content(db)


@router.get("/published-content")
def show_published_content(
      db: Session = Depends(get_db)
):
      return get_by_published(db)

@router.get("/Un-published-content")
def show_unpublished_content(
      db: Session = Depends(get_db)
):
      return get_by_un_published(db)

@router.get("/{content_type}")
def show_by_type_content(
      content_type: ContentType,
      db: Session = Depends(get_db)
):
      return get_by_type_service(db,content_type)

@router.patch("/publish/{content_id}")
def publish_content(
      content_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return publish_content_service(db,content_id)

@router.patch("/unpublish/{content_id}")
def un_publish_content(
      content_id: int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return un_publish_content_service(db,content_id)