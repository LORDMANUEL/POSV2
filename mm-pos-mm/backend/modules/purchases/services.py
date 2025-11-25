from sqlalchemy.orm import Session
from . import models, schemas
from modules.inventory import services as inventory_services
from modules.inventory.schemas import StockMoveCreate
from typing import List

def create_purchase_order(db: Session, po: schemas.PurchaseOrderCreate, user_id: int, branch_id: int):
    db_po = models.PurchaseOrder(
        supplier_id=po.supplier_id,
        user_id=user_id,
        expected_at=po.expected_at
    )
    db.add(db_po)
    db.flush()

    for item in po.items:
        db_item = models.PurchaseItem(
            purchase_order_id=db_po.id,
            product_id=item.product_id,
            quantity_ordered=item.quantity_ordered,
            cost=item.cost
        )
        db.add(db_item)

    db.commit()
    db.refresh(db_po)
    return db_po

def receive_purchase_order_items(db: Session, po_id: int, items: List[schemas.ReceiveItem], branch_id: int):
    po = db.query(models.PurchaseOrder).filter(models.PurchaseOrder.id == po_id).first()
    if not po:
        raise ValueError("Purchase order not found")

    for item_in in items:
        po_item = db.query(models.PurchaseItem).filter(
            models.PurchaseItem.id == item_in.purchase_item_id,
            models.PurchaseItem.purchase_order_id == po_id
        ).first()

        if not po_item:
            raise ValueError(f"Purchase item {item_in.purchase_item_id} not found in this PO")

        if po_item.quantity_received + item_in.quantity > po_item.quantity_ordered:
            raise ValueError("Cannot receive more than ordered quantity")

        po_item.quantity_received += item_in.quantity

        # Update inventory
        stock_move = StockMoveCreate(
            change=item_in.quantity, # Positive change for a purchase
            type="PURCHASE",
            ref_id=str(po.id)
        )
        inventory_services.create_stock_move(db, po_item.product_id, branch_id, stock_move)

    # Update PO status
    total_ordered = sum(item.quantity_ordered for item in po.items)
    total_received = sum(item.quantity_received for item in po.items)

    if total_received >= total_ordered:
        po.status = models.POStatus.RECEIVED
    else:
        po.status = models.POStatus.PARTIALLY_RECEIVED

    db.commit()
    db.refresh(po)
    return po
