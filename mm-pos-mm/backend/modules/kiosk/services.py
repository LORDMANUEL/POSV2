from sqlalchemy.orm import Session
from . import models, schemas

def create_kiosk_order(db: Session, order: schemas.KioskOrderCreate):
    db_order = models.KioskOrder(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
