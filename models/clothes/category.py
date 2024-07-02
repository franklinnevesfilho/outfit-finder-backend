from sqlalchemy import Column, Integer, String
from models.base import Base


""" Category Model

This is the Category model within the database
contains:
    - id: the id of the entity
    - name: the name of a category
    
@Author: Franklin Neves Filho
"""


class Category(Base):
    __tablename__ = 'Category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
