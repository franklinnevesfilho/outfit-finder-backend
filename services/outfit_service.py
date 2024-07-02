from models import (Outfit, CreateOutfit, User, Clothes, Occasion, Season, Weather)
from typing import Type
from utils import Service, Response, ResponseFactory
from sqlalchemy.orm.exc import NoResultFound


""" Outfit Service

The Outfit Service class is responsible for handling all the business logic for the outfits
within the application.

The OutfitService is responsible for joining the clothes to the outfit.

The OutfitService class contains the following methods:
    - get_user_outfits: get all outfits from a user
    - get_by_id: get outfit by id
    - get_all: get all outfits
    - create: create an outfit
    - update: update an outfit
    - delete: delete an outfit
    - join_outfit_clothes: join the clothes to the outfit

@Author: Franklin Neves Filho
"""


class OutfitService(Service):

    def get_user_outfits(self, user_id: int) -> Response:
        """
        Get all outfits from a user
        :param user_id:
        :return: {
            node: List[Outfit],
            errors: List[str]
        }
        """

        outfits = self.db.query(Outfit).filter(Outfit.user_id == user_id).all()
        if not outfits:
            return ResponseFactory.generate_not_found_response()

        outfits = [self.join_outfit_clothes(outfit) for outfit in outfits]

        return ResponseFactory.generate_ok_response(node=outfits)

    def get_by_id(self, item_id: int) -> Response:
        """
        Get outfit by id
        :param item_id: int
        :return: {
            node: Outfit,
            errors: List[str]
        }
        """

        try:
            outfit = self.db.query(Outfit).get(item_id)
            outfit = self.join_outfit_clothes(outfit)
            return ResponseFactory.generate_ok_response(node=outfit)

        except NoResultFound:
            return ResponseFactory.generate_not_found_response()

    def get_all(self) -> Response:
        """
        Get all outfits
        :return: {
            node: List[Outfit],
            errors: List[str]
        }
        """

        outfits = self.db.query(Outfit).all()
        if not outfits:
            return ResponseFactory.generate_not_found_response()

        outfits = [self.join_outfit_clothes(outfit) for outfit in outfits]

        return ResponseFactory.generate_ok_response(node=outfits)

    def create(self, data: CreateOutfit) -> Response:
        """
        Create an outfit
        :param data:
        :return: {
            node: Outfit,
            errors: List[str]
        }
        """

        # Check if user exists
        user_exists = self.db.query(User).filter(User.id == data.user_id).first()
        if not user_exists:
            return ResponseFactory.generate_error_response(message="User does not exist")

        # Check if occasion exists
        occasion_exists = self.db.query(Occasion).filter(Occasion.name == data.occasion).first()
        if not occasion_exists:
            return ResponseFactory.generate_error_response(message="Occasion does not exist")

        # Check if weather exists
        weather_exists = self.db.query(Weather).filter(Weather.name == data.weather).first()
        if not weather_exists:
            return ResponseFactory.generate_error_response(message="Weather does not exist")

        # Check if season exists
        season_exists = self.db.query(Season).filter(Season.name == data.season).first()
        if not season_exists:
            return ResponseFactory.generate_error_response(message="Season does not exist")

        # Check if clothes exist
        clothes = []
        for cloth in data.clothes:
            cloth_exists = self.db.query(Clothes).filter(Clothes.id == cloth).first()
            if not cloth_exists:
                return ResponseFactory.generate_error_response(message="Clothes do not exist")
            clothes.append(cloth_exists)

        outfit = Outfit(
            user_id=data.user_id,
            occasion=data.occasion,
            weather=data.weather,
            season=data.season
        )

        outfit.clothes = clothes

        self.db.add(outfit)
        self.db.commit()

        return ResponseFactory.generate_created_response(node=outfit)

    def update(self, item_id: int, data: CreateOutfit) -> Response:
        """
        Update an outfit
        :param item_id:
        :param data:
        :return: {
            node: Outfit,
            errors: List[str]
        }
        """

        outfit = self.db.query(Outfit).get(item_id)
        clothes = []
        for cloth in data.clothes:
            cloth_exists = self.db.query(Clothes).filter(Clothes.id == cloth).first()
            if not cloth_exists:
                return ResponseFactory.generate_error_response(message="Clothes do not exist")
            clothes.append(cloth_exists)

        outfit.user_id = data.user_id
        outfit.occasion = data.occasion
        outfit.weather = data.weather
        outfit.season = data.season
        outfit.clothes = clothes

        self.db.commit()

        return ResponseFactory.generate_ok_response(node=outfit)

    def delete(self, item_id: int) -> Response:
        """
        Delete an outfit
        :param item_id:
        :return: {
            node: str,
            errors: List[str]
        }
        """

        outfit = self.db.query(Outfit).get(item_id)
        if outfit is None:
            return ResponseFactory.generate_not_found_response()

        self.db.delete(outfit)
        self.db.commit()

        return ResponseFactory.generate_ok_response(node='Outfit deleted successfully')

    @staticmethod
    def join_outfit_clothes(outfit: Type[Outfit]):
        return {
            "id": outfit.id,
            "user_id": outfit.user_id,
            "occasion": outfit.occasion,
            "weather": outfit.weather,
            "season": outfit.season,
            "clothes": [cloth.id for cloth in outfit.clothes]
        }
