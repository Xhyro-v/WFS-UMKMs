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
        create_menu_service,
        update_menu_service,
        delete_menu_service,
        get_all_menu,
        get_menu,
        get_by_type_service,
        get_by_title_menu
)

router = APIRouter(
    prefix="/admin/menu",
    tags=["Admin Menus"]
)

templates = Jinja2Templates(directory="templates")

@router.post("/create")
def create_menu(
      data: MenuCreate,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return create_menu_service(
          db,
          data,
          current_admin
      )

@router.put("/update/{menu_id}")
def update_menu(
      data: MenuUpdate,
      menu_id : int,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return update_menu_service(db,menu_id,data)

@router.delete("/delete/{menu_id}")
def delete_menu(
      menu_id : int,
      db : Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return delete_menu_service(db, menu_id)


@router.get("/all")
def show_all_menu(
    db: Session = Depends(get_db)
):
    return get_all_menu(db)


@router.get("{/type/menu_type}")
def show_by_type(
    menu_type: MenuType,
    db: Session = Depends(get_db)
):
    return get_by_type_service(db,menu_type)

@router.get("/{menu_title}")
def show_by_title_menu(
      menu_title: str,
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
      return get_by_title_menu(db, menu_title)

@router.get("/{menu_id}")
def show_menu_by_id(
    menu_id: int,
    db: Session = Depends(get_db)
):
    return get_menu(db, menu_id)

