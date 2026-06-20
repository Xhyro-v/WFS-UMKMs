from sqlalchemy.orm import Session
from app.models.admin import Admin

def get_by_email(db:Session, email:str):
    return db.query(Admin).filter(Admin.email == email).first()


def create_admin(db:Session, admin:Admin):
    db.add(admin)
    db.commit()
    db.refresh(admin)
    return admin