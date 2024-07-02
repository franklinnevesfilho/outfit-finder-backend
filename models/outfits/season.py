from sqlalchemy import Column, Integer, String
from models.base import Base


""" Season Model

This is the Season model within the database
contains:
    - id: the id of the entity
    - name: the name of a season
    
@Author: Franklin Neves Filho
"""


class Season(Base):
    __tablename__ = 'Season'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
