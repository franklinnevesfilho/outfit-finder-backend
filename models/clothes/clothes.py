from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from models.base import Base


""" Clothes Model

This file contains the models used for the Clothes entity in the database.
There is a table which joins the clothes and colors tables, called clothes_colors.

the Clothes consists of:
    - id: the id of the clothes
    - user_id: the id of the user that created the clothes
    - image_url: the url of the image of the clothes
    - category: the category of the clothes
    - style: the style of the clothes
    - pattern: the pattern of the clothes
    - fabric: the fabric of the clothes
    - color: the color of the clothes
    
@Author: Franklin Neves Filho
"""


class Clothes(Base):
    __tablename__ = 'Clothes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    name = Column(String(50), unique=True, index=True)
    image_url = Column(String(100), unique=True, index=True)
    user = relationship("User", back_populates="clothes")
    category = Column(String(50), ForeignKey('Category.name'))
    style = Column(String(50), ForeignKey('Style.name'))
    pattern = Column(String(50), ForeignKey('Pattern.name'))
    fabric = Column(String(50), ForeignKey('Fabric.name'))
    color = Column(String(50), ForeignKey('Color.name'))


# Pydantic model for creating a clothes
class CreateClothes(BaseModel):
    user_id: int
    name: str
    image_url: str
    category: str
    style: str
    pattern: str
    fabric: str
    color: str
