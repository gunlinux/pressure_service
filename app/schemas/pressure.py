from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class PressureMeasurementBase(BaseModel):
    up: int
    down: int
    pulse: Optional[int] = None


class PressureMeasurementCreate(PressureMeasurementBase):
    pass


class PressureMeasurement(PressureMeasurementBase):
    id: int
    measurement_time: datetime
    user_id: int

    class Config:
        from_orm = True


class PressureMeasurementCreateList(BaseModel):
    telegram_nickname: str
    measurements: List[PressureMeasurementCreate]
