from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.schemas.pressure import PressureMeasurement, PressureMeasurementCreateList
from app.services.pressure_service import PressureMeasurementService
from app.db.session import get_db

router = APIRouter()
pressure_service = PressureMeasurementService()

@router.post("/", response_model=List[PressureMeasurement])
def create_pressure_measurements(
    data: PressureMeasurementCreateList, db: Session = Depends(get_db)
):
    return pressure_service.create_measurements(db=db, data=data)
