from fastapi import FastAPI
from utils import Database, S3Factory
from routers import register_routers
from services import register_services
from config import *


app = FastAPI()


# Dependency to get a database connection
database = Database(
    DATABASE_HOST,
    DATABASE_PORT,
    DATABASE_USER,
    DATABASE_PASSWORD,
    DATABASE_NAME)

s3 = S3Factory.get_s3(
    S3_TYPE,
    S3_HOST_URL,
    S3_ACCESS_KEY,
    S3_SECRET_KEY,
    {
        'secure': False
    })


# Dependency to get a database session
def get_db_session():
    db = database.get_db()
    try:
        yield next(db)
    finally:
        db.close()


# Register services with a database session
services = register_services(next(get_db_session()), s3)

register_routers(app, services)
