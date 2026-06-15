from app.db.base import Base
from app.db.session import engine
from app.models.admin import Admin
from app.models.content import Contents
from app.models.gallery import GalleryPhoto
from app.models.menu import Menu

Base.metadata.create_all(bind=engine)

print("Database initialized.")