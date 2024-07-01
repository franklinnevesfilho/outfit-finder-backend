from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Database:
    def __init__(self, db_host: str, user: str, password: str, db_name: str):
        self.db_url = f"mysql+pymysql://{user}:{password}@{db_host}/{db_name}"
        self.engine = create_engine(self.db_url)
        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_db(self):
        db = self.session_local()
        try:
            yield db
        finally:
            db.close()
