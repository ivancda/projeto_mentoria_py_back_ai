from sqlalchemy.orm import Session
from app.schemas.review import ReviewRequest, ReviewResponse, ReviewDB
from app.repositories.review_repository import ReviewRepository
from app.providers.provider_factory import get_provider

def review_code(review_request: ReviewRequest, db: Session) -> ReviewResponse:
    provider = get_provider()
    result = provider.review(review_request.code)
    repository = ReviewRepository(db)
    review_saved = repository.create(code=review_request.code, result=result)
    return ReviewResponse(status="success", review=review_saved.result)

def get_all_reviews(db: Session) -> list[ReviewDB]:
    repository = ReviewRepository(db)
    reviews = repository.get_all()
    return [ReviewDB.model_validate(review) for review in reviews]