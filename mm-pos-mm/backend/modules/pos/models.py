from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from core.database import Base
import datetime
import enum

class PaymentStatus(str, enum.Enum):
    PENDING = "pending"
    PAID = "paid"
    REFUNDED = "refunded"

class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    total = Column(Float, nullable=False)
    payment_status = Column(Enum(PaymentStatus), default=PaymentStatus.PAID)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    branch_id = Column(Integer, ForeignKey("branches.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=True)

    # Relationships
    user = relationship("User")
    branch = relationship("Branch")
    customer = relationship("Customer")
    items = relationship("SaleItem", back_populates="sale")
    payments = relationship("Payment", back_populates="sale")

class SaleItem(Base):
    __tablename__ = "sale_items"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Float, nullable=False)
    price = Column(Float, nullable=False) # Price at the time of sale

    sale_id = Column(Integer, ForeignKey("sales.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    # Relationships
    sale = relationship("Sale", back_populates="items")
    product = relationship("Product")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float, nullable=False)
    method = Column(String, nullable=False) # e.g., "cash", "card"

    sale_id = Column(Integer, ForeignKey("sales.id"))

    # Relationship
    sale = relationship("Sale", back_populates="payments")

class RegisterShift(Base):
    __tablename__ = "register_shifts"
    id = Column(Integer, primary_key=True, index=True)
    opening_amount = Column(Float, nullable=False)
    closing_amount = Column(Float, nullable=True)
    expected_amount = Column(Float, nullable=True)
    difference = Column(Float, nullable=True)
    opened_at = Column(DateTime, default=datetime.datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)

    user_open_id = Column(Integer, ForeignKey("users.id"))
    user_close_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    branch_id = Column(Integer, ForeignKey("branches.id"))

    # Relationships
    opener = relationship("User", foreign_keys=[user_open_id])
    closer = relationship("User", foreign_keys=[user_close_id])
    branch = relationship("Branch")
