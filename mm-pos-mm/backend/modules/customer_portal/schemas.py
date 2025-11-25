from pydantic import BaseModel
from typing import List
from modules.pos.schemas import Sale
from modules.crm.schemas import Customer

class CustomerDashboard(BaseModel):
    customer_details: Customer
    recent_orders: List[Sale]
    loyalty_points: float
