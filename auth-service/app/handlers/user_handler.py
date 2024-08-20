from sqlalchemy.orm import Session
from config.response_handler import Response
from ..utils import PasswordUtils
from .. import schemas
from .. import models


def create_user(user: schemas.UserCreate, db: Session) -> Response:
    hashed_password = PasswordUtils.encrypt(user.password)
    db_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return Response(node=db_user)


def update_user(user: schemas.UserCreate, db: Session):
    pass

def delete_user(user_id: str, db: Session):
    pass

def get_user(user_id: str, db: Session):
    pass

def get_users(db: Session):
    pass

def get_user_roles(user_id: str, db: Session):
    pass

def add_user_role(user_id: str, role: str, db: Session):
    pass

def remove_user_role(user_id: str, db: Session):
    pass