# lib pydantic serve para criar modelo de dados (schemas)
from pydantic import BaseModel

class ReviewRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    status: str
    review: str