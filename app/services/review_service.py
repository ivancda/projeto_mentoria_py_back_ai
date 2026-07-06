from sqlalchemy.orm import Session
from app.models.review import Review
from app.schemas.review import ReviewRequest, ReviewResponse
from app.repositories.review_repository import ReviewRepository

def review_code(review_request: ReviewRequest, db: Session) -> ReviewResponse:
    result = f"review realizada para o código: {review_request.code}"
    repository = ReviewRepository(db)
    review_saved = repository.create(code=review_request.code, result=result)
    return ReviewResponse(status="success", review=review_saved.result)

def get_all_reviews(db: Session) -> list[Review]:
    repository = ReviewRepository(db)
    reviews = repository.get_all()
    return reviews