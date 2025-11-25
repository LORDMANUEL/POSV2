from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from typing import List

from core.database import get_db
from core.auth.dependencies import require_role
from . import schemas, services, models

router = APIRouter()

@router.post("/settings", response_model=schemas.IntegrationSetting, status_code=status.HTTP_201_CREATED, dependencies=[Depends(require_role("Admin"))])
def create_integration_setting(setting: schemas.IntegrationSettingCreate, db: Session = Depends(get_db)):
    return services.create_integration_setting(db, setting)

@router.get("/settings", response_model=List[schemas.IntegrationSetting], dependencies=[Depends(require_role("Admin"))])
def read_integration_settings(branch_id: int, db: Session = Depends(get_db)):
    settings = db.query(models.IntegrationSetting).filter(models.IntegrationSetting.branch_id == branch_id).all()
    return settings

@router.post("/ecommerce/{platform}/sync", response_model=schemas.SyncLog, status_code=status.HTTP_202_ACCEPTED)
def trigger_ecommerce_sync(platform: str, branch_id: int, background_tasks: BackgroundTasks, db: Session = Depends(get_db), current_user: models.User = Depends(require_role("Admin"))):
    background_tasks.add_task(services.run_ecommerce_sync, db, platform, branch_id)
    return {"message": "E-commerce synchronization started in the background."}

@router.post("/delivery/{platform}/webhook")
def receive_delivery_webhook(platform: str, payload: dict):
    # This endpoint would validate the webhook and process the payload.
    # For example, it could create a new order in the POS or restaurant module.
    print(f"Received webhook from {platform}: {payload}")
    return {"status": "received"}
