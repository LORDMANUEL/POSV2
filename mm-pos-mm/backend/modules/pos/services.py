from sqlalchemy.orm import Session
from . import models, schemas
from modules.inventory import services as inventory_services
from modules.inventory.schemas import StockMoveCreate
from modules.crm import services as crm_services
from modules.crm.schemas import LoyaltyTxCreate
from core.events import post_event
import sum

def create_sale(db: Session, sale: schemas.SaleCreate):
    # Basic validation
    if not (sum(p.amount for p in sale.payments) >= sale.total):
        raise ValueError("The sum of payments must be greater than or equal to the total sale amount.")

    # Create the main sale record
    db_sale = models.Sale(
        total=sale.total,
        user_id=sale.user_id,
        branch_id=sale.branch_id,
        customer_id=sale.customer_id
    )
    db.add(db_sale)
    db.flush() # Use flush to get the sale ID before committing

    # Create sale items and update stock
    for item in sale.items:
        db_item = models.SaleItem(
            sale_id=db_sale.id,
            product_id=item.product_id,
            quantity=item.quantity,
            price=item.price
        )
        db.add(db_item)

        # Update inventory
        stock_move = StockMoveCreate(
            change=-item.quantity, # Negative change for a sale
            type="SALE",
            ref_id=str(db_sale.id)
        )
        inventory_services.create_stock_move(db, item.product_id, sale.branch_id, stock_move)

    # Create payment records
    for payment in sale.payments:
        db_payment = models.Payment(
            sale_id=db_sale.id,
            amount=payment.amount,
            method=payment.method
        )
        db.add(db_payment)

    # Add loyalty points if a customer is associated
    if sale.customer_id:
        # Simple rule: 1 point per dollar spent
        points_to_add = int(sale.total)
        loyalty_tx = LoyaltyTxCreate(
            change=points_to_add,
            type="EARN",
            ref_id=str(db_sale.id)
        )
        crm_services.add_loyalty_points(db, sale.customer_id, loyalty_tx)

    db.commit()
    db.refresh(db_sale)

    # Post an event to notify other parts of the system
    post_event("sale_created", sale_data=schemas.Sale.from_orm(db_sale).dict())

    return db_sale

def open_register(db: Session, shift: schemas.RegisterShiftCreate, user_id: int, branch_id: int):
    # Check for existing open shift in the same branch
    open_shift = db.query(models.RegisterShift).filter(
        models.RegisterShift.branch_id == branch_id,
        models.RegisterShift.closed_at == None
    ).first()
    if open_shift:
        raise ValueError("There is already an open register shift in this branch.")

    db_shift = models.RegisterShift(
        opening_amount=shift.opening_amount,
        user_open_id=user_id,
        branch_id=branch_id
    )
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift
