from app.core.database import get_db
from app.schemas.review import ReviewRequest, ReviewResponse, ReviewDB
from app.services.review_service import review_code, get_all_reviews
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter( )


@router.post("/review", response_model=ReviewResponse)
def review_endpoint(review_request: ReviewRequest, db: Session = Depends(get_db)):
    return review_code(review_request, db)

@router.get("/review", response_model=list[ReviewDB])
def get_reviews(db: Session = Depends(get_db)):
    reviews = get_all_reviews(db)
    return reviews