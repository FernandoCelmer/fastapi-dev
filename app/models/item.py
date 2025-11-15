"""
This module contains the item model.
"""
from datetime import datetime
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    String,
    Integer
)
from app.core.database import Base, engine


class Item(Base):
    """Item Model
    """

    __tablename__ = "item"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(75))
    description = Column(String(100))
    status = Column(Boolean, default=False)
    created_date = Column(
        DateTime,
        default=datetime.utcnow
    )
    update_date = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )


Base.metadata.create_all(bind=engine)
