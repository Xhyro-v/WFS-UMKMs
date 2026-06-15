from sqlalchemy import Column ,Integer, String ,ForeignKey, DateTime
from app.db.base import Base


class Admin(Base):
    __tablename__ = "admins"
    
    id = Column(Integer, primary_key=True, index=True)
    username =Column(String, unique=True)
    password_hash = Column(String)

