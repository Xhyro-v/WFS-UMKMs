from app.db.base import Base
from app.db.session import engine
from app.models.admin import Admin
from app.models.content import Content
from app.models.gallery import Gallery
from app.models.menu import Menu

Base.metadata.create_all(bind=engine)

print("Database initialized.")