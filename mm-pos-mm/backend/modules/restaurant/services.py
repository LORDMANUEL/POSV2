from sqlalchemy.orm import Session
from . import models, schemas

def create_table(db: Session, table: schemas.RestaurantTableCreate):
    db_table = models.RestaurantTable(**table.dict())
    db.add(db_table)
    db.commit()
    db.refresh(db_table)
    return db_table

def create_restaurant_order(db: Session, order: schemas.RestaurantOrderCreate):
    table = db.query(models.RestaurantTable).filter(models.RestaurantTable.id == order.table_id).first()
    if not table or table.status == models.TableStatus.OCCUPIED:
        raise ValueError("Table is not available")

    db_order = models.RestaurantOrder(
        table_id=order.table_id,
        user_id=order.user_id
    )
    db.add(db_order)
    db.flush()

    for item in order.items:
        db_item = models.RestaurantOrderItem(
            order_id=db_order.id,
            product_id=item.product_id,
            quantity=item.quantity,
            notes=item.notes
        )
        db.add(db_item)

    table.status = models.TableStatus.OCCUPIED

    db.commit()
    db.refresh(db_order)
    return db_order

def add_item_to_order(db: Session, order_id: int, item: schemas.RestaurantOrderItemCreate):
    order = db.query(models.RestaurantOrder).filter(models.RestaurantOrder.id == order_id).first()
    if not order or order.status != models.OrderStatus.OPEN:
        raise ValueError("Order is not open for new items")

    db_item = models.RestaurantOrderItem(
        order_id=order_id,
        product_id=item.product_id,
        quantity=item.quantity,
        notes=item.notes
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
