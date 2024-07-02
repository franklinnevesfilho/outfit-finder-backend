from sqlalchemy import Column, Integer, String
from models.base import Base


""" Pattern Model

This is the Pattern model within the database
contains:
    - id: the id of the entity
    - name: the name of a pattern
    
@Author: Franklin Neves Filho
"""


class Pattern(Base):
    __tablename__ = 'Pattern'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
