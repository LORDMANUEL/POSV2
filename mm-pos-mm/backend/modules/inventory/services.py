from sqlalchemy.orm import Session
from . import models, schemas
from modules.admin.models import Branch

def get_product_by_sku(db: Session, sku: str):
    return db.query(models.Product).filter(models.Product.sku == sku).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
        sku=product.sku,
        name=product.name,
        description=product.description,
        price=product.price,
        cost=product.cost,
        is_kit=product.is_kit,
        attributes=product.attributes
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    # Initialize stock for the new product
    initial_stock = models.Stock(
        product_id=db_product.id,
        branch_id=product.branch_id,
        quantity=product.initial_stock
    )
    db.add(initial_stock)
    db.commit()
    db.refresh(initial_stock)

    return db_product

def get_stock_level(db: Session, product_id: int, branch_id: int):
    return db.query(models.Stock).filter(
        models.Stock.product_id == product_id,
        models.Stock.branch_id == branch_id
    ).first()

def create_stock_move(db: Session, product_id: int, branch_id: int, move: schemas.StockMoveCreate):
    # 1. Get current stock
    stock = get_stock_level(db, product_id, branch_id)
    if not stock:
        # If stock level does not exist, create it.
        stock = models.Stock(product_id=product_id, branch_id=branch_id, quantity=0)
        db.add(stock)

    # 2. Update stock quantity
    stock.quantity += move.change

    # 3. Create stock move record
    db_move = models.StockMove(
        product_id=product_id,
        branch_id=branch_id,
        change=move.change,
        type=move.type,
        ref_id=move.ref_id
    )
    db.add(db_move)

    db.commit()
    db.refresh(db_move)
    return db_move
