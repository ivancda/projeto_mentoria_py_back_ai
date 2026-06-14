# lib pydantic serve para criar modelo de dados (schemas)
from pydantic import BaseModel

from datetime import datetime

class ReviewRequest(BaseModel):
    code: str

class ReviewResponse(BaseModel):
    status: str
    review: str

class ReviewDB(BaseModel):
    id: int
    code: str
    result: str
    created_at: datetime

    # from_attributes = True: diz ao Pydantic para ler os atributos do objeto SQLAlchemy.
    model_config = {"from_attributes": True}