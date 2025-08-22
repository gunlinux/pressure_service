from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base import Base


class PressureMeasurement(Base):
    __tablename__ = "pressure_measurements"

    id = Column(Integer, primary_key=True, index=True)
    up = Column(Integer, nullable=False)
    down = Column(Integer, nullable=False)
    pulse = Column(Integer, nullable=True)
    measurement_time = Column(DateTime, server_default=func.now())
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="measurements")
