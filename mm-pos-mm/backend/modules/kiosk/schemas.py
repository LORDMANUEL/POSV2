from pydantic import BaseModel
from typing import List, Dict, Any
from datetime import datetime

class KioskOrderCreate(BaseModel):
    items: List[Dict[str, Any]]
    total: float
    branch_id: int

class KioskOrder(KioskOrderCreate):
    id: int
    status: str
    created_at: datetime
    class Config: orm_mode = True
