from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from passlib.hash import bcrypt

from app.repositories.admin_repository import get_by_email
from app.models.admin import Admin

def authenticate_admin(db, email, password):
    admin = get_by_email(db, email)
    if not admin:
        return None

    if admin.password_hash != admin.password_hash:
        return None

    return admin

def register_admin(db,data ,bcrypt):
    if data.password != data.confirm_password:
        raise HTTPException(
            status_code=400,
            detail="Password dan konfirmasi password tidak sama."
        )

    password_hash = bcrypt.hash(data.password)

    new_admin = Admin(
        username=data.username,
        email=data.email,
        password_hash=password_hash
    )

    try:
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Username atau email sudah terdaftar."
        )

    return {"message":"Registrasi berhasil",
            "username": new_admin.username}