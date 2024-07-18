from abc import ABC
from .singleton_pattern import SingletonMeta
from sqlalchemy.orm import Session


class Service(ABC, metaclass=SingletonMeta):
    def __init__(self, db: Session = None):
        self.db = db

