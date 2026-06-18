from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from app.db.session import get_db
from app.schemas.admin import AdminLogin, AdminRegister
from app.services.admin_service import authenticate_admin, register_admin, login_admin



router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)



@router.post("/registration")
def register(data : AdminRegister,
             db:Session = Depends(get_db)):
    return register_admin(db,data)


@router.post("/login")
def login(
    data: AdminLogin,
    db: Session = Depends(get_db)
):
    return login_admin(db, data)