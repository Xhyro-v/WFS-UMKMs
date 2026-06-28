from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from sqlalchemy import Enum as SQLEnum
from app.db.base import Base
from app.enums.menu_type import MenuType

class Menu(Base):
    __tablename__ = "menus"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    description = Column(String,nullable=True)
    image_path = Column(String(256),nullable=False)
    menu_type = Column(
        SQLEnum(MenuType),
        nullable=False,
    )
    is_published = Column(Boolean, default=False,nullable=False)
    uploaded_by = Column(
    Integer,
    ForeignKey("admins.id"),
    nullable=False
    )