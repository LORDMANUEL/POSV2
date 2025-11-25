from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services, models
from modules.admin.schemas import User as AdminUser

router = APIRouter()

@router.post("/sales", response_model=schemas.Sale, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Cajero"))])
def create_sale(sale: schemas.SaleCreate, db: Session = Depends(get_db)):
    try:
        return services.create_sale(db=db, sale=sale)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/sales", response_model=List[schemas.Sale], dependencies=[Depends(require_role("Gerente"))])
def read_sales(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    sales = db.query(models.Sale).order_by(models.Sale.created_at.desc()).offset(skip).limit(limit).all()
    return sales

@router.get("/sales/{sale_id}", response_model=schemas.Sale, dependencies=[Depends(get_current_user)])
def read_sale(sale_id: int, db: Session = Depends(get_db)):
    db_sale = db.query(models.Sale).filter(models.Sale.id == sale_id).first()
    if db_sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return db_sale

@router.post("/register/open", response_model=schemas.RegisterShift, status_code=status.HTTP_201_CREATED)
def open_register(shift: schemas.RegisterShiftCreate, current_user: AdminUser = Depends(require_role("Cajero")), db: Session = Depends(get_db)):
    try:
        return services.open_register(db=db, shift=shift, user_id=current_user.id, branch_id=current_user.branch.id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/register/close", dependencies=[Depends(require_role("Cajero"))])
def close_register(close_data: schemas.RegisterShiftClose, db: Session = Depends(get_db)):
    # This endpoint's logic would be complex, calculating expected amounts
    # from sales and comparing with the closing amount. For now, it's a placeholder.
    return {"message": "Register closed successfully (logic to be fully implemented)."}
