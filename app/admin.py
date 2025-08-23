from typing import ClassVar, Any
from sqladmin import Admin, ModelView

from app.db.models.pressure import PressureMeasurement
from app.db.models.user import User


class UserAdmin(ModelView, model=User):
    column_list: ClassVar[list[Any]] = [User.id, User.telegram_nickname]  # pyright: ignore[reportIncompatibleVariableOverride]


class PressureAdmin(ModelView, model=PressureMeasurement):
    column_list: ClassVar[list[Any]] = [  # pyright: ignore[reportIncompatibleVariableOverride]
        PressureMeasurement.id,
        PressureMeasurement.up,
        PressureMeasurement.down,
        PressureMeasurement.pulse,
    ]


def init_admin(app, engine):
    admin = Admin(app, engine)
    admin.add_view(UserAdmin)
    admin.add_view(PressureAdmin)
