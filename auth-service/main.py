from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.exceptions import RequestValidationError
from config.config import logger
from config.response_handler import JsonResponse, validation_exception_handler, Response
from app import models, schemas, userHandler, JWT
from app.database import db_config

models.Base.metadata.create_all(bind=db_config.db.engine)

app = FastAPI(
    default_response_class=JsonResponse,
    exception_handlers={RequestValidationError: validation_exception_handler}
)

# Get - for Testing
@app.get("/", tags=["Health"])
def health_check() -> Response:
    return Response(node="Auth Service is up and running", status=200)

@app.post("/users", tags=["users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(db_config.get_db)):
    return userHandler.create_user(user, db)


# @app.post("/token", tags=["auth"])
# def login(user: schemas.UserLogin):


@app.get("/verify", tags=["auth"])
def verify(user: str = Depends(JWT.get_current_user)):
    return Response(node=user, status=200)

roles = [
    "admin",
    "user",
    "guest"
]

def db_init(db_session: Session):
    for role in roles:
        existing_role = db_session.query(models.Role).filter(models.Role.name == role).first()
        if not existing_role:
            new_role = models.Role(name=role)
            db_session.add(new_role)
        else:
            logger.info(f"Role {role} already exists")
    db_session.commit()
    logger.info("Roles initialized")

db_init(db_config.get_db())

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)