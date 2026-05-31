# lib pydantic serve para criar modelo de dados (schemas)
from pydantic import BaseModel

class ReviewRequest(BaseModel):
    code: str
    # campo language é opcional
    language: str | None = None 

class ReviewResponse(BaseModel):
    status: str
    review: str