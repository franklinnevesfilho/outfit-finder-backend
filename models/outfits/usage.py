from sqlalchemy import Column, Integer, String
from models.base import Base


""" Usage Model

This is the Usage model within the database
contains:
    - id: the id of the entity
    - name: the name of an occasion
    
@Author: Franklin Neves Filho
"""


class Usage(Base):
    __tablename__ = 'Usage'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
