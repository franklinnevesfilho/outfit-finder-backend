from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from models.base import Base


""" Outfit Model

This file contains the models used for the Outfit entity in the database.
There is a table which joins the clothes and outfits tables, called outfits_clothes.

the Outfit consists of:
    - id: the id of the outfit
    - user_id: the id of the user that created the outfit
    - usage: the usage for the outfit
    - weather: the weather for the outfit
    - season: the season for the outfit
    - clothes: the clothes that are part of the outfit
    
@Author: Franklin Neves Filho
"""


outfit_clothes_association = Table(
    'outfits_clothes', Base.metadata,
    Column('outfit_id', Integer, ForeignKey('Outfit.id')),
    Column('clothes_id', Integer, ForeignKey('Clothes.id'))
)


class Outfit(Base):
    __tablename__ = 'Outfit'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship("User", back_populates="outfits")
    usage = Column(String(100), ForeignKey('Usage.name'))
    weather = Column(String(100), ForeignKey('Weather.name'))
    season = Column(String(100), ForeignKey('Season.name'))
    clothes = relationship("Clothes", secondary=outfit_clothes_association)


class CreateOutfit(BaseModel):
    user_id: int
    usage: str
    season: str
    weather: str
    clothes: list[int]
