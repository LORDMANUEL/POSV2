from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import get_db
from core.auth.dependencies import get_current_user
from . import schemas, services

router = APIRouter()

@router.get("/dashboard", response_model=schemas.CustomerDashboard)
def get_dashboard(current_user: dict = Depends(get_current_user), db: Session = Depends(get_db)):
    # This assumes customer login is handled and linked to a crm customer record.
    # For now, we'll use the user's ID as the customer ID.
    dashboard = services.get_customer_dashboard(db, current_user.id)
    if not dashboard:
        raise HTTPException(status_code=404, detail="Customer not found")
    return dashboard
