from app.schemas.review import ReviewRequest

def review_code(review_request: ReviewRequest) -> str:
    # f string do python equivalente a template string do JS
    return f"review realizada para o código: {review_request.code}, linguagem: {review_request.language}"