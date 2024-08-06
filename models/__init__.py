from .user import *
from .clothes import *
from .outfits import *
from .prediction import *
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
    'Usage', 'Season', 'Weather',
    'Base', 'ClothesPredictionRequest', 'Gender'
]
