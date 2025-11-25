from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import schemas, services

router = APIRouter()

@router.post("/order", response_model=schemas.KioskOrder)
def create_order(order: schemas.KioskOrderCreate, db: Session = Depends(get_db)):
    return services.create_kiosk_order(db, order)
