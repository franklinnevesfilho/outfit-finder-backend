from sqlalchemy.orm import Session

class Handler:
    def __init__(self, db: Session):
        self.db = db
