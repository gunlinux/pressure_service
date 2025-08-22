from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserCreate


class UserService:
    def get_user_by_telegram_nickname(self, db: Session, telegram_nickname: str) -> User:
        return db.query(User).filter(User.telegram_nickname == telegram_nickname).first()

    def create_user(self, db: Session, user: UserCreate) -> User:
        db_user = User(id=user.id, telegram_nickname=user.telegram_nickname)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
