from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# GiftCard Schemas
class GiftCardBase(BaseModel):
    initial_amount: float

class GiftCardCreate(GiftCardBase):
    customer_id: Optional[int] = None

class GiftCard(GiftCardBase):
    id: int
    code: str
    current_balance: float
    is_active: bool
    issued_at: datetime
    expires_at: Optional[datetime]

    class Config:
        orm_mode = True

# CreditNote Schemas
class CreditNoteBase(BaseModel):
    initial_amount: float
    customer_id: int
    origin_sale_id: Optional[int] = None

class CreditNoteCreate(CreditNoteBase):
    pass

class CreditNote(CreditNoteBase):
    id: int
    current_balance: float
    is_active: bool
    issued_at: datetime

    class Config:
        orm_mode = True
