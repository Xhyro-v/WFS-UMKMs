from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.menu import Menu
from app.schemas.menu import MenuCreate, MenuUpdate
from app.enums.menu_type import MenuType
from app.repositories.menu_repository import (
      get_by_id,
      get_by_type,
      get_all,
      get_by_title,
      create_menu, 
      update_menu, 
      delete_menu,
      get_by_published_title,
      get_by_published_id,
      get_by_published_type,
      get_by_published_menus
)

def create_menu_service(
      db: Session,
      data:MenuCreate,
      current_admin
):
    if data is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid data"
        )

    if len(data.title) > 40:
        raise HTTPException(
            status_code=400,
            detail="Max 40 character !"
          )
    if not data.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Fill menu name !!"
          )
    
    if data.price <= 0:
        raise HTTPException(
            status_code=401,
            detail="Fill menu price !!"
        )
    
    if len(data.description) == 0 :
          raise HTTPException(
              status_code=401,
              detail="Fill menu description !"
          )
    if len(data.description) > 100 :
          raise HTTPException(
              status_code=401,
              detail="Max 100 character!"
          )
    
    new_menu = Menu(
        title=data.title,
        price=data.price,
        description=data.description,
        image_path=data.image_path,
        menu_type=data.menu_type,
        uploaded_by=current_admin.id
    )
    
    try:
        create_menu(db,new_menu)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="The menu has been made!!"
        )
    
    return {"message":"Menu successfully created",
            "Menu": new_menu.title,
            "uploaded_by":new_menu.uploaded_by
    }

def update_menu_service(
      db: Session,
      menu_id: int,
      data: MenuUpdate
):
      menu = get_by_id(db, menu_id)
      
      if not menu:
          raise HTTPException(
              status_code=404,
              detail="Menu not found"
          )
      
      menu.title = data.title
      menu.price = data.price
      menu.description = data.description
      menu.image_path = data.image_path
      menu.menu_type = data.menu_type
      
      try:
          updated_menu = update_menu(db, menu)
      
      except IntegrityError:
          db.rollback()
      
          raise HTTPException(
              status_code=409,
              detail="Theres a mistake while updating!"
          )
      
      return {
          "message": "Menu successfully updated",
          "menu": updated_menu.title
      }


def delete_menu_service(
      db: Session,
      menu_id: int
):
      menu = get_by_id(db, menu_id)
      
      if not menu:
          raise HTTPException(
              status_code=404,
              detail="Menu not found"
          )
      
      delete_menu(db, menu)
      
      return {
          "message": "Menu successfully deleted"
      }


def get_menu(db: Session ,menu_id: int):
      menu = get_by_id(db, menu_id)
      if not menu :
        raise HTTPException(
            status_code=404,
            detail="Menu not found"
        )
      return menu

def get_by_title_menu(
      db: Session,
      menu_title : str
):
      menu = get_by_title(db,menu_title)
      if not menu:
            raise HTTPException(
                  status_code=404,
                  detail="Menu not found"
            )
      return menu

def get_all_menu(db: Session):
      return get_all(db)

def get_by_type_service(db:Session, menu_type:MenuType):
      menu = get_by_type(db, menu_type)
      if not menu :
            raise HTTPException(
                status_code=422,
                detail="Menu not found in this type!"
            )
      return menu

#——————————————————————PUBLICSERVICE—————————————————————————

def get_id_by_published_menu(
      db: Session,
      menu_id: int
):
      menu = get_by_published_id(db, menu_id)
      if not menu :
        raise HTTPException(
            status_code=404,
            detail="Menu not found"
        )
      return menu

def get_all_published_menus(db: Session):
      return get_by_published_menus(db)

def get_by_published_type_service(
      db:Session,
      menu_type:MenuType
):
      menu = get_by_published_type(db, menu_type)
      if not menu :
            raise HTTPException(
                status_code=422,
                detail="Menu not found in this type!"
            )
      return menu

def get_by_published_title_service(
      db: Session,
      menu_title: str
):
      menu = get_by_published_title(db, menu_title)
      
      if not menu:
            raise HTTPException(
                  status_code=404,
                  detail="Menu not found!"
            )
      return menu
      
      