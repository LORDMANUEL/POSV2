from sqlalchemy.orm import Session
from . import models, schemas

def get_customer_by_email(db: Session, email: str):
    return db.query(models.Customer).filter(models.Customer.email == email).first()

def get_customer_by_phone(db: Session, phone: str):
    return db.query(models.Customer).filter(models.Customer.phone_number == phone).first()

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(
        full_name=customer.full_name,
        email=customer.email,
        phone_number=customer.phone_number
    )
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def add_loyalty_points(db: Session, customer_id: int, transaction: schemas.LoyaltyTxCreate):
    customer = db.query(models.Customer).filter(models.Customer.id == customer_id).first()
    if not customer:
        return None # Or raise an exception

    # Update customer points
    customer.loyalty_points += transaction.change

    # Create loyalty transaction record
    db_tx = models.LoyaltyTx(
        customer_id=customer_id,
        change=transaction.change,
        type=transaction.type,
        ref_id=transaction.ref_id
    )
    db.add(db_tx)

    db.commit()
    db.refresh(customer)
    return customer
