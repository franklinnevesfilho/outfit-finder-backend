from sqlalchemy import Column, Integer, String
from models.base import Base


""" Weather Model

This is the Weather model within the database
contains:
    - id: the id of the entity
    - name: the name of a weather
    
@Author: Franklin Neves Filho
"""


class Weather(Base):
    __tablename__ = 'Weather'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
