from pydantic import BaseModel
from typing import List, Dict, Any

class Report(BaseModel):
    title: str
    data: Dict[str, Any]

class FraudAlert(BaseModel):
    transaction_id: str
    reason: str
    severity: str

class Recommendation(BaseModel):
    recommendation: str
    confidence: float
