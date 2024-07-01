from sqlalchemy import Column, Integer, String
from models.base import Base


class Fabric(Base):
    __tablename__ = 'Fabric'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
