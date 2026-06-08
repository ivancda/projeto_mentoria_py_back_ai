from typing import List
from sqlalchemy.orm import Session
from app.models.review import Review

class ReviewRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        code: str,
        result: str
    ) -> Review:

        db_review = Review(
            code=code,
            result=result
        )

        self.db.add(db_review)

        self.db.commit()

        self.db.refresh(db_review)

        return db_review

    def get_all(self) -> List[Review]:
        return self.db.query(Review).all()