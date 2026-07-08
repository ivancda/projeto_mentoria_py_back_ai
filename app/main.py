from fastapi import FastAPI
from app.api.review import router as review_router
from app.api.frontend import router as frontend_router
from app.core.database import Base, engine
from app.models.review import Review
from fastapi.staticfiles import StaticFiles

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(review_router)
app.include_router(frontend_router)