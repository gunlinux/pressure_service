from sqlalchemy.orm import Session
from app.db.models.pressure import PressureMeasurement
from app.schemas.pressure import PressureMeasurementCreate
from app.services.user_service import UserService
from fastapi import HTTPException


class PressureMeasurementService:
    def __init__(self, user_service: UserService | None = None):
        self.user_service = user_service or UserService()

    def create_measurements(
        self,
        db: Session,
        user_id: int,
        measurements_data: list[PressureMeasurementCreate],
    ):
        user = self.user_service.get_user_by_id(db, user_id=user_id)
        if not user:
            raise HTTPException(status_code=404, detail='User not found')

        measurements = []
        for measurement_data in measurements_data:
            db_measurement = PressureMeasurement(
                up=measurement_data.up,
                down=measurement_data.down,
                pulse=measurement_data.pulse,
                user_id=user.id,
            )
            measurements.append(db_measurement)

        db.add_all(measurements)
        db.commit()
        # The created objects are not automatically refreshed with the data from the DB
        # so we need to refresh them to get the IDs and timestamps
        for m in measurements:
            db.refresh(m)
        return measurements
