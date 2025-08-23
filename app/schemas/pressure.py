from pydantic import BaseModel
from datetime import datetime


class PressureMeasurementBase(BaseModel):
    up: int
    down: int
    pulse: int | None = None


class PressureMeasurementCreate(PressureMeasurementBase):
    pass


class PressureMeasurement(PressureMeasurementBase):
    id: int
    measurement_time: datetime
    user_id: int

    class Config:
        from_orm = True


class PressureMeasurementCreateList(BaseModel):
    measurements: list[PressureMeasurementCreate]
