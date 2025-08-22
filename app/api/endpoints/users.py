from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.schemas.user import User, UserCreate
from app.services.user_service import UserService
from app.db.session import get_db

router = APIRouter()
user_service = UserService()

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
