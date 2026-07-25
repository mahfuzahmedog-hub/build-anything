"""SQLAlchemy models."""

from datetime import UTC, datetime

from sqlalchemy import Column, DateTime, Integer, String

from app.database import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, default="")
    created_at = Column(DateTime, default=lambda: datetime.now(UTC))
