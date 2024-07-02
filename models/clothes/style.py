from sqlalchemy import Column, Integer, String
from models.base import Base


""" Style Model

This is the Style model within the database
contains:
    - id: the id of the entity
    - name: the name of a style
    
@Author: Franklin Neves Filho
"""


class Style(Base):
    __tablename__ = 'Style'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
