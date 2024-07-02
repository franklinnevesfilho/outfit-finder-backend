from sqlalchemy import Column, Integer, String
from models.base import Base


""" Gender Model

This is the Gender model within the database
contains:
    - id: the id of the entity
    - name: the name of a gender

@Author: Franklin Neves Filho
"""


class Gender(Base):
    __tablename__ = 'Gender'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
