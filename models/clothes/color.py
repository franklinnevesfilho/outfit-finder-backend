from sqlalchemy import Column, Integer, String
from models.base import Base


class Color(Base):
    __tablename__ = 'Color'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
