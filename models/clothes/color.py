from sqlalchemy import Column, Integer, String
from models.base import Base


""" Color Model

This is the Color model within the database
contains:
    - id: the id of the entity
    - name: the name of a color
    
@Author: Franklin Neves Filho 
"""


class Color(Base):
    __tablename__ = 'Color'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
