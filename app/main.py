from fastapi import FastAPI
from app.api.review import router as review_router

app = FastAPI()
app.include_router(review_router)

