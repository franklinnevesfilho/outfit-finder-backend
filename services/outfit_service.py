from models import (Outfit, CreateOutfit, User, Clothes, Occasion, Season, Weather)
from typing import Type
from utils import Service, Response, ResponseFactory
from sqlalchemy.orm.exc import NoResultFound


class OutfitService(Service):


    def get_user_outfits(self, user_id: int) -> Response:
        outfits = self.db.query(Outfit).filter(Outfit.user_id == user_id).all()
        if not outfits:
            return ResponseFactory.generate_not_found_response()

        outfits = [self.join_outfit_clothes(outfit) for outfit in outfits]

        return ResponseFactory.generate_ok_response(node=outfits)

    def get_by_id(self, item_id: int) -> Response:
        try:
            outfit = self.db.query(Outfit).get(item_id)
            outfit = self.join_outfit_clothes(outfit)
            return ResponseFactory.generate_ok_response(node=outfit)

        except NoResultFound:
            return ResponseFactory.generate_not_found_response()

    def get_all(self) -> Response:
        outfits = self.db.query(Outfit).all()
        if not outfits:
            return ResponseFactory.generate_not_found_response()

        outfits = [self.join_outfit_clothes(outfit) for outfit in outfits]

        return ResponseFactory.generate_ok_response(node=outfits)

    def create(self, data: CreateOutfit) -> Response:
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
        outfit = self.db.query(Outfit).get(item_id)

        # Check if clothes exist
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
