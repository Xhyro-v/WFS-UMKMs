from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from db.base import Base

class GaleryPhoto(Base):
    __tablename__ = "galery_photos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,nullable=False)
    description = Column(String,nullable=True)
    image_path = Column(String,nullable=False)
    created_at = Column(DateTime,nullable=False, default=datetime.utcnow)
    uploaded_by = Column(
          Integer,
          ForeignKey("admins.id"),
          nullable=False
    )