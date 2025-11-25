from pydantic import BaseModel
from typing import Optional, Dict, Any
from datetime import datetime
from .models import SyncStatus

# IntegrationSetting Schemas
class IntegrationSettingBase(BaseModel):
    platform: str
    auth_data: Dict[str, Any]
    is_active: bool = True
    branch_id: int

class IntegrationSettingCreate(IntegrationSettingBase):
    pass

class IntegrationSetting(IntegrationSettingBase):
    id: int

    class Config:
        orm_mode = True

# SyncLog Schemas
class SyncLogBase(BaseModel):
    platform: str
    operation: str
    status: SyncStatus
    details: Optional[Dict[str, Any]] = None

class SyncLogCreate(SyncLogBase):
    pass

class SyncLog(SyncLogBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
