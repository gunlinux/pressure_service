from sqlalchemy.orm import Session
from app.db.models.pressure import PressureMeasurement
from app.schemas.pressure import PressureMeasurementCreateList
from app.services.user_service import UserService
from fastapi import HTTPException


class PressureMeasurementService:
    def __init__(self, user_service: UserService = UserService()):
        self.user_service = user_service

    def create_measurements(self, db: Session, data: PressureMeasurementCreateList):
        user = self.user_service.get_user_by_telegram_nickname(db, telegram_nickname=data.telegram_nickname)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")

        measurements = []
        for measurement_data in data.measurements:
            db_measurement = PressureMeasurement(
                up=measurement_data.up,
                down=measurement_data.down,
                pulse=measurement_data.pulse,
                user_id=user.id
            )
            measurements.append(db_measurement)

        db.add_all(measurements)
        db.commit()
        # The created objects are not automatically refreshed with the data from the DB
        # so we need to refresh them to get the IDs and timestamps
        for m in measurements:
            db.refresh(m)
        return measurements
