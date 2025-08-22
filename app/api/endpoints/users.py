from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import User, UserCreate
from app.services.user_service import UserService
from app.db.session import get_db
from app.schemas.pressure import PressureMeasurement, PressureMeasurementCreate
from app.services.pressure_service import PressureMeasurementService
from typing import List

router = APIRouter()
user_service = UserService()
pressure_service = PressureMeasurementService()

@router.post("/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = user_service.get_user_by_telegram_nickname(db, telegram_nickname=user.telegram_nickname)
    if db_user:
        raise HTTPException(status_code=400, detail="Telegram nickname already registered")
    try:
        return user_service.create_user(db=db, user=user)
    except IntegrityError:
        # This is a fallback, the check above should be sufficient
        db.rollback()
        raise HTTPException(status_code=400, detail="Telegram nickname already registered")

@router.post("/{user_id}/pressure/", response_model=List[PressureMeasurement])
def create_pressure_measurements_for_user(
    user_id: int,
    measurements: List[PressureMeasurementCreate],
    db: Session = Depends(get_db)
):
    return pressure_service.create_measurements(db=db, user_id=user_id, measurements_data=measurements)