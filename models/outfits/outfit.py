from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from models.base import Base
from models.clothes.clothes import Clothes

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
    occasion = Column(String(100), ForeignKey('Occasion.name'))
    weather = Column(String(100), ForeignKey('Weather.name'))
    season = Column(String(100), ForeignKey('Season.name'))
    clothes = relationship("Clothes", secondary=outfit_clothes_association)


class CreateOutfit(BaseModel):
    user_id: int
    occasion: str
    season: str
    weather: str
    clothes: list[int]
