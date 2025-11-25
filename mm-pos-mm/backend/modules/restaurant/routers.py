from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services, models

router = APIRouter()

@router.post("/tables", response_model=schemas.RestaurantTable, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_table(table: schemas.RestaurantTableCreate, db: Session = Depends(get_db)):
    return services.create_table(db, table)

@router.get("/tables", response_model=List[schemas.RestaurantTable], dependencies=[Depends(get_current_user)])
def read_tables(branch_id: int, db: Session = Depends(get_db)):
    tables = db.query(models.RestaurantTable).filter(models.RestaurantTable.branch_id == branch_id).all()
    return tables

@router.post("/orders", response_model=schemas.RestaurantOrder, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Mesero"))])
def create_order(order: schemas.RestaurantOrderCreate, db: Session = Depends(get_db)):
    try:
        return services.create_restaurant_order(db, order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/orders/{order_id}/item", response_model=schemas.RestaurantOrderItem, dependencies=[Depends(require_role("Mesero"))])
def add_item_to_order(order_id: int, item: schemas.RestaurantOrderItemCreate, db: Session = Depends(get_db)):
    try:
        return services.add_item_to_order(db, order_id, item)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/orders/{order_id}", response_model=schemas.RestaurantOrder, dependencies=[Depends(get_current_user)])
def read_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(models.RestaurantOrder).filter(models.RestaurantOrder.id == order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
