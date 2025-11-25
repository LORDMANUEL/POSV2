from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime
from .models import POStatus
from modules.inventory.schemas import Product

# Supplier Schemas
class SupplierBase(BaseModel):
    name: str
    contact_info: Optional[str] = None
    data: Optional[Dict[str, Any]] = None

class SupplierCreate(SupplierBase):
    pass

class Supplier(SupplierBase):
    id: int

    class Config:
        orm_mode = True

# PurchaseItem Schemas
class PurchaseItemBase(BaseModel):
    product_id: int
    quantity_ordered: float
    cost: float

class PurchaseItemCreate(PurchaseItemBase):
    pass

class PurchaseItem(PurchaseItemBase):
    id: int
    quantity_received: float
    product: Product

    class Config:
        orm_mode = True

# PurchaseOrder Schemas
class PurchaseOrderBase(BaseModel):
    supplier_id: int
    expected_at: Optional[datetime] = None

class PurchaseOrderCreate(PurchaseOrderBase):
    items: List[PurchaseItemCreate]
    user_id: int

class PurchaseOrderUpdate(BaseModel):
    status: Optional[POStatus] = None

class PurchaseOrder(PurchaseOrderBase):
    id: int
    status: POStatus
    created_at: datetime
    user_id: int
    items: List[PurchaseItem] = []

    class Config:
        orm_mode = True

# Schema for receiving items
class ReceiveItem(BaseModel):
    purchase_item_id: int
    quantity: float
