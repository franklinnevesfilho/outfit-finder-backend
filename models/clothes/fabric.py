from sqlalchemy import Column, Integer, String
from models.base import Base


""" Fabric Model

This is the Fabric model within the database
contains:
    - id: the id of the entity
    - name: the name of a fabric
    
@Author: Franklin Neves Filho
"""


class Fabric(Base):
    __tablename__ = 'Fabric'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True)
