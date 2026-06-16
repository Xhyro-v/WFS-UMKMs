from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.admin import AdminLogin
from app.services.admin_service import authenticate_admin

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/login")
def login(data: AdminLogin, db: Session = Depends(get_db)):
    admin = authenticate_admin(
        db,
        data.email,
        data.password
    )

    if admin is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )

    return {
        "message": "Login successful",
        "username": admin.username
    }