from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .middleware import setup_middleware

# Import all module routers
from modules.pos.routers import router as pos_router
from modules.inventory.routers import router as inventory_router
from modules.purchases.routers import router as purchases_router
from modules.crm.routers import router as crm_router
from modules.admin.routers import router as admin_router
from modules.ai.routers import router as ai_router
from modules.signage.routers import router as signage_router
from modules.kiosk.routers import router as kiosk_router
from modules.customer_portal.routers import router as customer_portal_router
from modules.loyalty.routers import router as loyalty_router
from modules.restaurant.routers import router as restaurant_router
from modules.integrations.routers import router as integrations_router

app = FastAPI(
    title="MM (POS VENTA MULTI)",
    description="Sistema POS empresarial modular.",
    version="1.0.0",
)

# CORS Middleware Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Setup custom middleware
setup_middleware(app)

# Create a master router for the /api/v1 prefix
api_router = APIRouter(prefix="/api/v1")

# Include module routers in the master router
api_router.include_router(pos_router, prefix="/pos", tags=["POS"])
api_router.include_router(inventory_router, prefix="/inventory", tags=["Inventory"])
api_router.include_router(purchases_router, prefix="/purchases", tags=["Purchases"])
api_router.include_router(crm_router, prefix="/crm", tags=["CRM"])
api_router.include_router(admin_router, prefix="/admin", tags=["Admin"])
api_router.include_router(ai_router, prefix="/ai", tags=["AI"])
api_router.include_router(signage_router, prefix="/signage", tags=["Signage"])
api_router.include_router(kiosk_router, prefix="/kiosk", tags=["Kiosk"])
api_router.include_router(customer_portal_router, prefix="/customer", tags=["Customer Portal"])
api_router.include_router(loyalty_router, prefix="/loyalty", tags=["Loyalty"])
api_router.include_router(restaurant_router, prefix="/restaurant", tags=["Restaurant"])
api_router.include_router(integrations_router, prefix="/integrations", tags=["Integrations"])

# Include the master router in the main app
app.include_router(api_router)

@app.get("/", tags=["Health Check"])
def read_root():
    """Health check endpoint to confirm the API is running."""
    return {"status": "ok", "message": "Welcome to the MM POS API"}
