from fastapi import FastAPI
from app.api.review import router as review_router
from app.api.frontend import router as frontend_router
from app.api.health import router as health_router
from app.core.database import Base, engine
from app.core.logging_config import setup_logging
from app.models.review import Review
from fastapi.staticfiles import StaticFiles
from contextlib import asynccontextmanager

# setup_logging() no lifespan pra rodar depois do Uvicorn, garantindo que a configuração de logging seja aplicada corretamente.
@asynccontextmanager
async def lifespan(app: FastAPI):
    setup_logging()
    yield

Base.metadata.create_all(bind=engine)

app = FastAPI(lifespan=lifespan)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(health_router)
app.include_router(review_router)
app.include_router(frontend_router)