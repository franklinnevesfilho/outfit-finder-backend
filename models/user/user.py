from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel, EmailStr
from models.base import Base


""" User Model / Create User Model

This file contains the User model and the CreateUser model.
Which are used to represent the User entity in the database and to create a new User.

@Author: Franklin Neves Filho
"""


class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    gender = Column(String, ForeignKey('Gender.name'))
    password = Column(String(200))
    clothes = relationship("Clothes", back_populates='user')
    outfits = relationship("Outfit", back_populates='user')


# Pydantic model for creating a user
class CreateUser(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    password: str
    gender: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str

