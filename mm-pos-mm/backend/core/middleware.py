import time
import logging
from fastapi import Request, status
from fastapi.responses import JSONResponse

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def add_process_time_header(request: Request, call_next):
    """
    Middleware to add a custom X-Process-Time header to all responses,
    which contains the time taken to process the request.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    logger.info(f"Request {request.method} {request.url.path} processed in {process_time:.4f} seconds")
    return response

async def global_exception_handler(request: Request, call_next):
    """
    Middleware for global exception handling. Catches any unhandled exceptions
    and returns a standardized JSON error response.
    """
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Unhandled exception for request {request.method} {request.url.path}: {e}", exc_info=True)
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"detail": "An unexpected internal server error occurred."},
        )

def setup_middleware(app):
    """Attaches all middleware to the FastAPI app instance."""
    app.middleware("http")(add_process_time_header)
    app.middleware("http")(global_exception_handler)
