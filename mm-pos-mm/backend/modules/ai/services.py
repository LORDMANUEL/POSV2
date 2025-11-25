def get_intelligent_report():
    return {"title": "Daily Sales Report", "data": {"total_sales": 1500.75, "growth": 0.05}}

def get_fraud_alerts():
    return [{"transaction_id": "SALE123", "reason": "High value refund", "severity": "high"}]

def get_recommendations():
    return [{"recommendation": "Restock product SKU-456", "confidence": 0.92}]
