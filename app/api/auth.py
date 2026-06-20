from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from app.db.session import get_db
from app.schemas.admin import AdminLogin, AdminRegister
from app.services.admin_service import authenticate_admin, register_admin, login_admin
from app.dependencies.auth import get_current_admin ,oauth2_scheme



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

@router.get("/me")
def me(
    current_admin = Depends(get_current_admin)
):
    return {
        "id": current_admin.id,
        "username": current_admin.username,
        "email": current_admin.email
    }

@router.get("/test")
def test(
    token: str = Depends(oauth2_scheme)
):
    return {
        "token": token
    }