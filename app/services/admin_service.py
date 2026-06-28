from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

from app.repositories.admin_repository import get_by_email
from app.services.auth_service import create_access_token
from app.schemas.admin import AdminLogin
from app.models.admin import Admin

def authenticate_admin(db, email, password):
    admin = get_by_email(db, email)
    if not admin:
        return None

    #jaga-jaga 
    if not bcrypt.verify(password,admin.password_hash):
        return None

    return admin

def login_admin(db: Session,data: AdminLogin):
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
    
    token = create_access_token(
        {
        "sub":admin.email
      }
    )
    
    return {
      "access_token": token,
      "token_type": "bearer"
    }


def register_admin(db,data):

    if len(data.username) < 2:
        raise HTTPException(
          status_code=400,
          detail="Username too short,min 5 character!"
        )
      
    if len(data.username) > 25:
        raise HTTPException(
          status_code=400,
          detail="Username too long,mix 25 character"
        )
      
    if len(data.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password min 8 character !"
        )

    if len(data.password) > 20:
        raise HTTPException(
            status_code=400,
            detail="Password max 20 character !"
        )



    if data.password != data.confirm_password:
        raise HTTPException(
            status_code=400,
            detail="Password or password confirmation not same!!"
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
            detail="Username or email already registraded."
        )

    return {"message":"Successfully registraded",
            "username": new_admin.username}