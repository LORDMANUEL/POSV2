from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services, models
from modules.admin.schemas import User as AdminUser

router = APIRouter()

@router.post("/suppliers", response_model=schemas.Supplier, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_supplier(supplier: schemas.SupplierCreate, db: Session = Depends(get_db)):
    db_supplier = models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()
    db.refresh(db_supplier)
    return db_supplier

@router.get("/suppliers", response_model=List[schemas.Supplier], dependencies=[Depends(get_current_user)])
def read_suppliers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    suppliers = db.query(models.Supplier).offset(skip).limit(limit).all()
    return suppliers

@router.post("/orders", response_model=schemas.PurchaseOrder, status_code=status.HTTP_201_CREATED)
def create_purchase_order(po: schemas.PurchaseOrderCreate, current_user: AdminUser = Depends(require_role("Comprador")), db: Session = Depends(get_db)):
    return services.create_purchase_order(db, po, user_id=current_user.id, branch_id=current_user.branch.id)

@router.get("/orders", response_model=List[schemas.PurchaseOrder], dependencies=[Depends(get_current_user)])
def read_purchase_orders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pos = db.query(models.PurchaseOrder).order_by(models.PurchaseOrder.created_at.desc()).offset(skip).limit(limit).all()
    return pos

@router.put("/orders/{po_id}/receive", response_model=schemas.PurchaseOrder)
def receive_items(po_id: int, items: List[schemas.ReceiveItem], current_user: AdminUser = Depends(require_role("Almacén")), db: Session = Depends(get_db)):
    try:
        return services.receive_purchase_order_items(db, po_id, items, branch_id=current_user.branch.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
