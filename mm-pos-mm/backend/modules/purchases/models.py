from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, JSON, Enum
from sqlalchemy.orm import relationship
from core.database import Base
import datetime
import enum

class POStatus(str, enum.Enum):
    DRAFT = "draft"
    SENT = "sent"
    PARTIALLY_RECEIVED = "partially_received"
    RECEIVED = "received"
    CANCELLED = "cancelled"

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    contact_info = Column(String)
    data = Column(JSON, nullable=True) # For extra flexible data

    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(POStatus), default=POStatus.DRAFT)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    expected_at = Column(DateTime, nullable=True)

    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    supplier = relationship("Supplier", back_populates="purchase_orders")
    user = relationship("User")
    items = relationship("PurchaseItem", back_populates="purchase_order")

class PurchaseItem(Base):
    __tablename__ = "purchase_items"
    id = Column(Integer, primary_key=True, index=True)
    quantity_ordered = Column(Float, nullable=False)
    quantity_received = Column(Float, default=0)
    cost = Column(Float, nullable=False)

    purchase_order_id = Column(Integer, ForeignKey("purchase_orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    purchase_order = relationship("PurchaseOrder", back_populates="items")
    product = relationship("Product")
