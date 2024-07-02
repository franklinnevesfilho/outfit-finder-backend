from sqlalchemy import Column, Integer, String
from models.base import Base


""" Occasion Model

This is the Occasion model within the database
contains:
    - id: the id of the entity
    - name: the name of an occasion
    
@Author: Franklin Neves Filho
"""


class Occasion(Base):
    __tablename__ = 'Occasion'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
