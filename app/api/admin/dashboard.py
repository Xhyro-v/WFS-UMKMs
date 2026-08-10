from fastapi import APIRouter, HTTPException, Depends,Request
from fastapi.responses import RedirectResponse, HTMLResponse 
from sqlalchemy.orm import Session


from app.db.session import get_db
from app.dependencies.auth import get_current_admin
from app.services.dashboard_service import get_dashboard_summary

router = APIRouter(
    prefix="/admin/dashboard/summary",
    tags=["Admin Dashboard Summary"]
)

@router.get("/Menu")
def get_menu_total_data(
      db: Session = Depends(get_db),
      current_admin = Depends(get_current_admin)
):
    return get_dashboard_summary(db)