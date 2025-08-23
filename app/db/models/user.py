from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from app.db.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=False)
    telegram_nickname = Column(String, unique=True, index=True, nullable=False)
    registration_data = Column(DateTime, server_default=func.now())

    measurements = relationship('PressureMeasurement', back_populates='user')
