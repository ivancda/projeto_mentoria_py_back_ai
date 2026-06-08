from app.models.review import Review
from app.schemas.review import ReviewRequest
from app.repositories.review_repository import ReviewRepository

def review_code(review_request: ReviewRequest, db) -> Review:
    # f string do python equivalente a template string do JS
    result = f"review realizada para o código: {review_request.code}"

    repository = ReviewRepository(db)
    
    review_saved = repository.create(code=review_request.code, result=result)

    return review_saved

def get_all_reviews(db):
    repository = ReviewRepository(db)
    reviews = repository.get_all()
    return reviews