import datetime

from app.core.database import Base
from sqlalchemy import Column, Integer, Text, DateTime

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    code = Column(Text)
    result = Column(Text)
    created_at = Column(DateTime, default = lambda: datetime.datetime.now(datetime.timezone.utc))