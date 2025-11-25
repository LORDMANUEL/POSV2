from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import datetime

# Product Schemas
class ProductBase(BaseModel):
    sku: str
    name: str
    description: Optional[str] = None
    price: float
    cost: Optional[float] = None
    is_kit: bool = False
    attributes: Optional[Dict[str, Any]] = None

class ProductCreate(ProductBase):
    initial_stock: float = 0
    branch_id: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    cost: Optional[float] = None
    attributes: Optional[Dict[str, Any]] = None

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True

# Stock Schemas
class StockBase(BaseModel):
    quantity: float
    product_id: int
    branch_id: int

class Stock(StockBase):
    id: int
    product: Product

    class Config:
        orm_mode = True

# StockMove Schemas
class StockMoveBase(BaseModel):
    change: float
    type: str
    ref_id: Optional[str] = None
    product_id: int
    branch_id: int

class StockMoveCreate(BaseModel):
    change: float
    type: str
    ref_id: Optional[str] = None

class StockMove(StockMoveBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
