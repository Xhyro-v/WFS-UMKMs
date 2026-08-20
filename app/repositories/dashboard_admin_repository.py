from sqlalchemy.orm import Session

from app.models.menu import Menu
from app.enums.menu_type import MenuType
from app.enums.content_type import ContentType



def get_menu_summary(db: Session):
    total_menu = (
        db.query(Menu)
        .count()
    )

    total_menu_makanan = (
        db.query(Menu)
        .filter(Menu.menu_type == MenuType.MAKANAN)
        .count()
    )

    total_menu_minuman = (
        db.query(Menu)
        .filter(Menu.menu_type == MenuType.MINUMAN)
        .count()
    )

    total_unpublished_menu = (
        db.query(Menu)
        .filter(Menu.is_published == False)
        .count()
    )

    total_unpublished_makanan = (
        db.query(Menu)
        .filter(
            Menu.menu_type == MenuType.MAKANAN,
            Menu.is_published == False,
        )
        .count()
    )

    total_unpublished_minuman = (
        db.query(Menu)
        .filter(
            Menu.menu_type == MenuType.MINUMAN,
            Menu.is_published == False,
        )
        .count()
    )

    total_published_menu = (
        db.query(Menu)
        .filter(Menu.is_published == True)
        .count()
    )

    total_published_makanan = (
        db.query(Menu)
        .filter(
            Menu.menu_type == MenuType.MAKANAN,
            Menu.is_published == True,
        )
        .count()
    )

    total_published_minuman = (
        db.query(Menu)
        .filter(
            Menu.menu_type == MenuType.MINUMAN,
            Menu.is_published == True,
        )
        .count()
    )

    return {
        "total": total_menu,
        "published": total_published_menu,
        "unpublished": total_unpublished_menu,
        "makanan": {
            "total": total_menu_makanan,
            "published": total_published_makanan,
            "unpublished": total_unpublished_makanan,
        },
        "minuman": {
            "total": total_menu_minuman,
            "published": total_published_minuman,
            "unpublished": total_unpublished_minuman,
        },
    }
