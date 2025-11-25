from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from modules.inventory.schemas import Product
from modules.admin.schemas import User, Branch
from modules.crm.schemas import Customer

# Payment Schemas
class PaymentBase(BaseModel):
    amount: float
    method: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int

    class Config:
        orm_mode = True

# SaleItem Schemas
class SaleItemBase(BaseModel):
    product_id: int
    quantity: float
    price: float

class SaleItemCreate(SaleItemBase):
    pass

class SaleItem(SaleItemBase):
    id: int
    product: Product

    class Config:
        orm_mode = True

# Sale Schemas
class SaleBase(BaseModel):
    total: float
    customer_id: Optional[int] = None

class SaleCreate(SaleBase):
    items: List[SaleItemCreate]
    payments: List[PaymentCreate]
    user_id: int
    branch_id: int

class Sale(SaleBase):
    id: int
    created_at: datetime
    user: User
    branch: Branch
    customer: Optional[Customer]
    items: List[SaleItem] = []
    payments: List[Payment] = []

    class Config:
        orm_mode = True

# Register Shift Schemas
class RegisterShiftBase(BaseModel):
    opening_amount: float

class RegisterShiftCreate(RegisterShiftBase):
    pass

class RegisterShiftClose(BaseModel):
    closing_amount: float

class RegisterShift(RegisterShiftBase):
    id: int
    opened_at: datetime
    closed_at: Optional[datetime]
    user_open_id: int
    user_close_id: Optional[int]
    branch_id: int

    class Config:
        orm_mode = True
