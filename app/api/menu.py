from fastapi import APIRouter, HTTPException, Depends,Request
from fastapi.responses import RedirectResponse, HTMLResponse 
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.menu import Menu
from app.schemas.menu import MenuCreate,MenuResponse
from app.services.menu_service import create_menu_service, get_all_menu, get_menu
from app.dependencies.auth import get_current_admin

router = APIRouter(
    prefix="/menu",
    tags=["Menus"]
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

@router.get(
    "/{menu_id}"
)
def show_menu(
    menu_id: int,
    db: Session = Depends(get_db)
):
    return get_menu(db, menu_id)