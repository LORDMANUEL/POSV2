from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from core.database import Base
import datetime
import enum

class TableStatus(str, enum.Enum):
    AVAILABLE = "available"
    OCCUPIED = "occupied"
    RESERVED = "reserved"

class OrderStatus(str, enum.Enum):
    OPEN = "open"
    BILLED = "billed"
    PAID = "paid"
    CANCELLED = "cancelled"

class RestaurantTable(Base):
    __tablename__ = "restaurant_tables"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    capacity = Column(Integer, default=0)
    status = Column(Enum(TableStatus), default=TableStatus.AVAILABLE)

    branch_id = Column(Integer, ForeignKey("branches.id"))
    branch = relationship("Branch")
    orders = relationship("RestaurantOrder", back_populates="table")

class RestaurantOrder(Base):
    __tablename__ = "restaurant_orders"
    id = Column(Integer, primary_key=True, index=True)
    status = Column(Enum(OrderStatus), default=OrderStatus.OPEN)
    opened_at = Column(DateTime, default=datetime.datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)

    table_id = Column(Integer, ForeignKey("restaurant_tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    table = relationship("RestaurantTable", back_populates="orders")
    user = relationship("User")
    items = relationship("RestaurantOrderItem", back_populates="order")

class RestaurantOrderItem(Base):
    __tablename__ = "restaurant_order_items"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    notes = Column(String, nullable=True)

    order_id = Column(Integer, ForeignKey("restaurant_orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))

    order = relationship("RestaurantOrder", back_populates="items")
    product = relationship("Product")
