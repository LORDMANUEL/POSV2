from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import get_current_user
from . import schemas, services, models

router = APIRouter()

@router.post("/customers", response_model=schemas.Customer, status_code=status.HTTP_201_CREATED, dependencies=[Depends(get_current_user)])
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    if customer.email:
        db_customer_by_email = services.get_customer_by_email(db, email=customer.email)
        if db_customer_by_email:
            raise HTTPException(status_code=400, detail="Email already registered")
    if customer.phone_number:
        db_customer_by_phone = services.get_customer_by_phone(db, phone=customer.phone_number)
        if db_customer_by_phone:
            raise HTTPException(status_code=400, detail="Phone number already registered")

    return services.create_customer(db=db, customer=customer)

@router.get("/customers", response_model=List[schemas.Customer], dependencies=[Depends(get_current_user)])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    customers = db.query(models.Customer).offset(skip).limit(limit).all()
    return customers

@router.get("/customers/{customer_id}", response_model=schemas.Customer, dependencies=[Depends(get_current_user)])
def read_customer(customer_id: int, db: Session = Depends(get_db)):
    db_customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return db_customer

@router.post("/customers/{customer_id}/loyalty", response_model=schemas.Customer, dependencies=[Depends(get_current_user)])
def add_loyalty_points(customer_id: int, transaction: schemas.LoyaltyTxCreate, db: Session = Depends(get_db)):
    customer = services.add_loyalty_points(db, customer_id, transaction)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer
