from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models.userModel import User
from schemas.user import UserSignupRequest
from utils.encryption import encypt_password


def get_user(db: Session):
    return db.query(User).all()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, body: UserSignupRequest):
    try:
        user = User(name=body.name, email=body.email, password=encypt_password(body.password))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error creating user: {str(e)}")
        raise

    finally:
        db.close()
