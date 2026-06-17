from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from passlib.hash import bcrypt

from app.repositories.admin_repository import get_by_email
from app.models.admin import Admin

def authenticate_admin(db, email, password):
    admin = get_by_email(db, email)
    if not admin:
        return None

    #jaga-jaga 
    if not bcrypt.verify(password,admin.password_hash):
        return None

    return admin

def register_admin(db,data):

    if len(data.username) < 2:
        raise HTTPException(
          status_code=400,
          detail="Username terlalu pendek!,minimal 5 karakter"
        )
      
    if len(data.username) > 25:
        raise HTTPException(
          status_code=400,
          detail="Username terlalu panjang!,maksimal 25 karakter"
        )
      
    if len(data.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password mininal 8 karakter !"
        )

    if len(data.password) > 20:
        raise HTTPException(
            status_code=400,
            detail="Password maksimal 20 karakter !"
        )



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