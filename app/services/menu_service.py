from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.menu import menu
from app.repositories.menu_repository import get_by_id, get_by_type, get_all, create_menu, update_menu, delete_menu
from app.schemas.menu import MenuCreate, MenuUpdate

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
            detail="Maksimal 40 huruf !"
          )
    if not data.title.strip():
        raise HTTPException(
            status_code=400,
            detail="Isi nama menu !!"
          )
    
    if data.price <= 0:
        raise HTTPException(
            status_code=401,
            detail="Isi harga menu !!"
        )
    
    if len(data.description) == 0 :
          raise HTTPException(
              status_code=401,
              detail="Isi deskripsi menu !"
          )
    if len(data.description) > 100 :
          raise HTTPException(
              status_code=401,
              detail="Maksimal 100 huruf !"
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
            detail="Menu sudah ada!!"
        )
    
    return {"message":"Menu berhasil ditambahkan",
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
              detail="Menu tidak ditemukan"
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
              detail="Terjadi kesalahan saat update menu"
          )
      
      return {
          "message": "Menu berhasil diupdate",
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
              detail="Menu tidak ditemukan"
          )
      
      delete_menu(db, menu)
      
      return {
          "message": "Menu berhasil dihapus"
      }


def get_menu(db: Session ,menu_id: int):
      menu = get_by_id(db, menu_id)
      if not menu :
        raise HTTPException(
            status_code=404,
            detail="Tidak ada menu"
        )
      return menu

def get_all_menu(db: Session):
      return get_all(db)

def get_by_type_service(db:Session, menu_type:MenuType):
      menu = get_by_type(db, menu_type)
      if not menu :
            raise HTTPException(
                status_code=422,
                detail="Menu tidak tersedia !"
            )
      return menu

