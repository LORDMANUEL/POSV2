from fastapi import APIRouter
from . import services, schemas

router = APIRouter()

@router.get("/reports", response_model=schemas.Report)
def get_report():
    return services.get_intelligent_report()

@router.get("/fraud-alerts", response_model=list[schemas.FraudAlert])
def get_alerts():
    return services.get_fraud_alerts()

@router.get("/recommendations", response_model=list[schemas.Recommendation])
def get_recommendations():
    return services.get_recommendations()
