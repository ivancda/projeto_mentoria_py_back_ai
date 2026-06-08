from fastapi import FastAPI
from app.api.review import router as review_router
from app.core.database import Base, engine
from app.models.review import Review

Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(review_router)

