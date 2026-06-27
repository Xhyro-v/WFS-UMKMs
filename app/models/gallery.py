from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean
from app.db.base import Base

class Gallery(Base):
    __tablename__ = "galleries"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,nullable=False)
    description = Column(Text,nullable=True)
    image_path = Column(String(256),nullable=False)
    created_at = Column(DateTime,nullable=False, default=datetime.utcnow)
    is_published = Column(Boolean, default=False,nullable=False)
    uploaded_by = Column(
          Integer,
          ForeignKey("admins.id"),
          nullable=False
    )