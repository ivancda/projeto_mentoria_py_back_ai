from app.core.database import get_db
from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.review_service import review_code, get_all_reviews
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter( )

@router.post("/review")
def review_endpoint(review_request: ReviewRequest, db: Session = Depends(get_db)) -> ReviewResponse:
    resultado = review_code(review_request, db)
    return ReviewResponse(status="success", review=resultado.result)

@router.get("/review")
def get_reviews(db: Session = Depends(get_db)):
    reviews = get_all_reviews(db)
    return reviews