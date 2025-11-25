from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import get_current_user, require_role
from . import schemas, services, models
from modules.admin.schemas import User as AdminUser

router = APIRouter()

@router.post("/products", response_model=schemas.Product, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = services.get_product_by_sku(db, sku=product.sku)
    if db_product:
        raise HTTPException(status_code=400, detail="SKU already registered")
    return services.create_product(db=db, product=product)

@router.get("/products", response_model=List[schemas.Product], dependencies=[Depends(get_current_user)])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@router.get("/stock/{product_id}", response_model=schemas.Stock, dependencies=[Depends(get_current_user)])
def read_stock(product_id: int, branch_id: int, db: Session = Depends(get_db)):
    stock = services.get_stock_level(db, product_id, branch_id)
    if not stock:
        raise HTTPException(status_code=404, detail="Stock level not found for this product and branch")
    return stock

@router.post("/movements/{product_id}", response_model=schemas.StockMove, dependencies=[Depends(require_role("Admin"))])
def create_stock_movement(product_id: int, branch_id: int, move: schemas.StockMoveCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return services.create_stock_move(db, product_id, branch_id, move)
