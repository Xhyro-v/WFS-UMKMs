from datetime import datetime
from sqlalchemy import Column, String ,Integer,Boolean, DateTime, ForeignKey, Text
from sqlalchemy import Enum as SQLEnum
from app.db.base import Base
from app.enums.content_type import ContentType


class Content(Base):
    __tablename__ = "contents"
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String, nullable=False)
    content_type = Column(
        SQLEnum(ContentType),
        nullable=False,
        default=ContentType.NEWS
    )
    description = Column(Text,nullable=False)
    image_path = Column(String,nullable=True)
    location = Column(String,nullable=True)
    is_published = Column(Boolean,default=False,nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    uploaded_by = Column(
          Integer,
          ForeignKey("admins.id"),
          nullable=False
    )