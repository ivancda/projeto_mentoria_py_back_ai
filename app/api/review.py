from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.review_service import review_code
from fastapi import APIRouter

router = APIRouter()

@router.post("/review")
def review_endpoint(review_request: ReviewRequest) -> ReviewResponse:
    resultado = review_code(review_request)
    return ReviewResponse(status="success", review=resultado)