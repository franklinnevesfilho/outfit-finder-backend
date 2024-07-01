from fastapi import FastAPI, Depends
from typing import Annotated
from models import *
from utils.database import Database
from routers import register_routers
from services import register_services
from config import *

app = FastAPI()


# Dependency to get a database connection
database = Database(DATABASE_HOST, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME)


# Dependency to get a database session
def get_db_session():
    db = database.get_db()
    try:
        yield next(db)
    finally:
        db.close()


# Register services with a database session
services = register_services(next(get_db_session()))

register_routers(app, services)
