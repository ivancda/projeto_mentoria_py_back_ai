import logging
import httpx
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.schemas.health import HealthResponse, ServiceStatus
from app.core.config import settings
from app.core.database import get_db

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/health", response_model=HealthResponse)
def health_check(db: Session = Depends(get_db)):
    try:
        httpx.get(f"{settings.OLLAMA_URL}/api/tags", timeout=5).raise_for_status()
        ollama = ServiceStatus(status="ok")
    except Exception as e:
        logger.warning("Ollama health check failed: %s", e)
        ollama = ServiceStatus(status=f"error: {e}")

    try:
        db.execute(text("SELECT 1"))
        db_status = ServiceStatus(status="ok")
    except Exception as e:
        logger.warning("DB health check failed: %s", e)
        db_status = ServiceStatus(status=f"error: {e}")

    healthy = ollama.status == "ok" and db_status.status == "ok"
    body = HealthResponse(status="healthy" if healthy else "unhealthy", ollama=ollama, db=db_status)
    return JSONResponse(content=body.model_dump(), status_code=200 if healthy else 503)
