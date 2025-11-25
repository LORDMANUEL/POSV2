from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class GiftCard(Base):
    __tablename__ = "gift_cards"
    id = Column(Integer, primary_key=True, index=True)
    code = Column(String, unique=True, index=True, nullable=False)
    initial_amount = Column(Float, nullable=False)
    current_balance = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    issued_at = Column(DateTime, default=datetime.datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)
    customer = relationship("Customer")

class CreditNote(Base):
    __tablename__ = "credit_notes"
    id = Column(Integer, primary_key=True, index=True)
    initial_amount = Column(Float, nullable=False)
    current_balance = Column(Float, nullable=False)
    is_active = Column(Boolean, default=True)
    issued_at = Column(DateTime, default=datetime.datetime.utcnow)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    origin_sale_id = Column(Integer, ForeignKey("sales.id"), nullable=True) # e.g., from a refund

    customer = relationship("Customer")
    sale = relationship("Sale")
