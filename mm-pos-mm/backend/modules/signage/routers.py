from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import get_db
from . import schemas, services, models

router = APIRouter()

@router.post("/content/ai-generate", response_model=schemas.SignageContent)
def generate_content(prompt: str):
    return services.generate_ai_content(prompt)

@router.get("/screens", response_model=list[schemas.Screen])
def get_screens(branch_id: int, db: Session = Depends(get_db)):
    return db.query(models.Screen).filter(models.Screen.branch_id == branch_id).all()
