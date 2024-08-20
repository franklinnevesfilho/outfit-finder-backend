from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config


class Database:
    def __init__(self, db_type, db_host, db_port, db_user, db_password, db_name):
        self.db_type = db_type
        self.db_host = db_host
        self.db_port = db_port
        self.db_user = db_user
        self.db_password = db_password
        self.db_name = db_name
        self.engine = None
        self._connect()

    def _connect(self):
        url = self._get_url()
        self.engine = create_engine(url)
        self._session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        session = self._session_local()
        try:
            yield session
        finally:
            session.close()

    def _get_url(self):
        if self.db_type == "mysql":
            return f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"
        else:
            config.logger.error(f"Unsupported database type: {self.db_type}")
            raise Exception(f"Unsupported database type: {self.db_type}")


# Usage
db = Database(
    db_type=config.DB_TYPE,
    db_host=config.DB_HOST,
    db_port=config.DB_PORT,
    db_user=config.DB_USER,
    db_password=config.DB_PASSWORD,
    db_name=config.DB_NAME,
)


# Dependency for FastAPI routes
def get_db():
    db_session = db.get_session()
    try:
        yield next(db_session)
    finally:
        db_session.close()

