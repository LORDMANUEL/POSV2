from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DateTime, JSON
from sqlalchemy.orm import relationship
from core.database import Base
import datetime

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    sku = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    cost = Column(Float, nullable=True)
    is_kit = Column(Boolean, default=False)
    attributes = Column(JSON, nullable=True) # e.g., {"color": "red", "size": "M"}

    # Relationships
    stock_levels = relationship("Stock", back_populates="product")
    stock_moves = relationship("StockMove", back_populates="product")
    # sale_items = relationship("SaleItem", back_populates="product") # Add when pos module is created

class Stock(Base):
    __tablename__ = "stock"
    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Float, nullable=False, default=0)

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)

    # Relationships
    product = relationship("Product", back_populates="stock_levels")
    branch = relationship("Branch") # Assumes Branch model exists in admin module

class StockMove(Base):
    __tablename__ = "stock_moves"
    id = Column(Integer, primary_key=True, index=True)
    change = Column(Float, nullable=False)
    type = Column(String, nullable=False) # e.g., SALE, PURCHASE, ADJUSTMENT
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    ref_id = Column(String, nullable=True) # e.g., sale_id, purchase_order_id

    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    branch_id = Column(Integer, ForeignKey("branches.id"), nullable=False)

    # Relationships
    product = relationship("Product", back_populates="stock_moves")
    branch = relationship("Branch")
