from sqlalchemy import Column, Integer, String, JSON, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class KioskOrder(Base):
    __tablename__ = "kiosk_orders"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending") # pending, paid, ready, collected
    items = Column(JSON, nullable=False)
    total = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    branch_id = Column(Integer, ForeignKey("branches.id"))
    branch = relationship("Branch")
