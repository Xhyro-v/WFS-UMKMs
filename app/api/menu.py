from fastapi import APIRouter, HTTPException, Depends,Request
from fastapi.responses import RedirectResponse, HTMLResponse 
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.menu import Menu
from app.enums.menu_type import MenuType
from app.schemas.menu import MenuCreate,MenuResponse,MenuUpdate
from app.dependencies.auth import get_current_admin
from app.services.menu_service import (
      get_id_by_published_menu,
      get_all_published_menus,
      get_by_published_type_service,
      get_by_published_title_service
)

router = APIRouter(
    prefix="/menu",
    tags=["Menus"]
)

templates = Jinja2Templates(directory="templates")


@router.get("/menus")
def show_all_menu(
    db: Session = Depends(get_db)
):
    return get_all_published_menus(db)


@router.get("{/type/menu_type}")
def show_by_type(
    menu_type: MenuType,
    db: Session = Depends(get_db)
):
    return get_by_published_type_servicee(db,menu_type)

@router.get("/{menu_title}")
def show_by_menu_title(
      menu_title: str,
      db: Session = Depends(get_db)
):
      return get_by_published_title_service(db, menu_title)


@router.get("/{menu_id}")
def show_menu_by_id(
    menu_id: int,
    db: Session = Depends(get_db)
):
    return get_id_by_published_menu(db, menu_id)

