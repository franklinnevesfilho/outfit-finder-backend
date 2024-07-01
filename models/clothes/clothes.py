from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from models.base import Base

clothes_color_association = Table(
    'clothes_colors', Base.metadata,
    Column('clothes_id', Integer, ForeignKey('Clothes.id')),
    Column('color_id', Integer, ForeignKey('Color.id'))
)


class Clothes(Base):
    __tablename__ = 'Clothes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship("User", back_populates="clothes")
    image_url = Column(String(100), unique=True, index=True)
    category = Column(String(50), ForeignKey('Category.name'))
    style = Column(String(50), ForeignKey('Style.name'))
    pattern = Column(String(50), ForeignKey('Pattern.name'))
    fabric = Column(String(50), ForeignKey('Fabric.name'))
    colors = relationship('Color', secondary=clothes_color_association)


# Pydantic model for creating a clothes
class CreateClothes(BaseModel):
    user_id: int
    image_url: str
    category: str
    style: str
    pattern: str
    fabric: str
    colors: list[int]
