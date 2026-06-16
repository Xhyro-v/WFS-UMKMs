from sqlalchemy.orm import Session
from app.models.admin import Admin

def get_by_email(db:Session, email:str):
    return db.query(Admin).filter(Admin.email == email).first()
