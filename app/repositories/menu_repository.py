from sqlalchemy.orm import Session
from app.models.menu import Menu


def get_by_title(db: Session, title: str):
    return 
        (db.query(Menu)
        .filter(Menu.title == title)
        .first()
    )

def get_by_type(db: Session, menu_type: MenuType):
    return (
        db.query(Menu)
        .filter(Menu.menu_type == menu_type)
        .all()
    )

def get_by_id(db: Session ,menu_id: int):
    return (
        db.query(Menu)
        .filter(Menu.id == menu_id)
        .first
    )

def get_all(db: Session):
    return (
        db.query(Menu)
        .all()
    )

def create_menu(db: Session , menu: Menu):
    db.add(menu)
    db.commit()
    db.refresh(menu)

    return menu

def delete_menu(db: Session , menu: Menu):
    db.delete(menu)
    db.commit()

    return menu

def update_menu(db: Session, menu: Menu):
    db.update(menu)
    db.commit()
    db.refresh(menu)
    return menus