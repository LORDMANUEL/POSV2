from sqlalchemy.orm import Session
from modules.crm import services as crm_services
from modules.pos.models import Sale

def get_customer_dashboard(db: Session, customer_id: int):
    customer = db.query(crm_services.models.Customer).filter(crm_services.models.Customer.id == customer_id).first()
    if not customer:
        return None

    recent_orders = db.query(Sale).filter(Sale.customer_id == customer_id).order_by(Sale.created_at.desc()).limit(5).all()

    return {
        "customer_details": customer,
        "recent_orders": recent_orders,
        "loyalty_points": customer.loyalty_points
    }
