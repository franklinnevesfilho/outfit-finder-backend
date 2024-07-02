from .user import *
from .clothes import *
from .outfits import *
from .base import Base

"""
Defining all available models in the application

@Author: Franklin Neves Filho
"""


__all__ = [
    'User', 'CreateUser', 'LoginUser',
    'Clothes', 'CreateClothes',
    'Category', 'Style', 'Pattern', 'Fabric', 'Color',
    'Outfit', 'CreateOutfit',
    'Occasion', 'Season', 'Weather',
    'Base',
]
