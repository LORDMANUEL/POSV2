from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .models import TableStatus, OrderStatus
from modules.inventory.schemas import Product

# RestaurantTable Schemas
class RestaurantTableBase(BaseModel):
    name: str
    capacity: int

class RestaurantTableCreate(RestaurantTableBase):
    branch_id: int

class RestaurantTableUpdate(BaseModel):
    status: Optional[TableStatus] = None

class RestaurantTable(RestaurantTableBase):
    id: int
    status: TableStatus
    branch_id: int

    class Config:
        orm_mode = True

# RestaurantOrderItem Schemas
class RestaurantOrderItemBase(BaseModel):
    product_id: int
    quantity: int
    notes: Optional[str] = None

class RestaurantOrderItemCreate(RestaurantOrderItemBase):
    pass

class RestaurantOrderItem(RestaurantOrderItemBase):
    id: int
    product: Product

    class Config:
        orm_mode = True

# RestaurantOrder Schemas
class RestaurantOrderBase(BaseModel):
    table_id: int

class RestaurantOrderCreate(RestaurantOrderBase):
    user_id: int
    items: List[RestaurantOrderItemCreate]

class RestaurantOrderUpdate(BaseModel):
    status: Optional[OrderStatus] = None

class RestaurantOrder(RestaurantOrderBase):
    id: int
    status: OrderStatus
    opened_at: datetime
    user_id: int
    items: List[RestaurantOrderItem] = []

    class Config:
        orm_mode = True
