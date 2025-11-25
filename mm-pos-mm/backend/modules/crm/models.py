from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=True)
    phone_number = Column(String, unique=True, index=True, nullable=True)
    full_name = Column(String, index=True)
    loyalty_points = Column(Float, default=0)

    # Relationships
    loyalty_transactions = relationship("LoyaltyTx", back_populates="customer")
    # sales = relationship("Sale", back_populates="customer") # Add when pos module is created

class LoyaltyTx(Base):
    __tablename__ = "loyalty_tx"
    id = Column(Integer, primary_key=True, index=True)
    change = Column(Float, nullable=False)
    type = Column(String, nullable=False) # e.g., EARN, REDEEM
    ref_id = Column(String, nullable=True) # e.g., sale_id
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)

    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)

    # Relationship
    customer = relationship("Customer", back_populates="loyalty_transactions")
