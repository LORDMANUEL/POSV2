from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, JSON, Enum
from sqlalchemy.orm import relationship
from core.database import Base
import datetime
import enum

class SyncStatus(str, enum.Enum):
    SUCCESS = "success"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"

class IntegrationSetting(Base):
    __tablename__ = "integration_settings"
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, nullable=False) # e.g., "woocommerce", "shopify"
    auth_data = Column(JSON, nullable=False) # API keys, secrets, etc.
    is_active = Column(Integer, default=True)

    branch_id = Column(Integer, ForeignKey("branches.id"))
    branch = relationship("Branch")

class SyncLog(Base):
    __tablename__ = "sync_logs"
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String, nullable=False)
    operation = Column(String, nullable=False) # e.g., "import_orders", "export_products"
    status = Column(Enum(SyncStatus), default=SyncStatus.IN_PROGRESS)
    details = Column(JSON, nullable=True) # e.g., {"imported": 10, "errors": 0}
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
