from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.menu import Menu
from app.service.menu_servive import create_menu_service 

router = APIRouter(
    prefix="/menu"
)