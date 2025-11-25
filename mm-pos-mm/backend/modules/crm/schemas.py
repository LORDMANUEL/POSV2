from pydantic import BaseModel, EmailStr
from typing import Optional, List
import datetime

# Customer Schemas
class CustomerBase(BaseModel):
    full_name: str
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None

class Customer(CustomerBase):
    id: int
    loyalty_points: float

    class Config:
        orm_mode = True

# Loyalty Transaction Schemas
class LoyaltyTxBase(BaseModel):
    change: float
    type: str
    ref_id: Optional[str] = None
    customer_id: int

class LoyaltyTxCreate(BaseModel):
    change: float
    type: str
    ref_id: Optional[str] = None

class LoyaltyTx(LoyaltyTxBase):
    id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True
