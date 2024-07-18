from sqlalchemy.orm import joinedload
from models import Clothes, CreateClothes, Category, Style, Pattern, Fabric, Color, Outfit
from utils import Service, Response, ResponseFactory
from .jwt_service import JwtService
from sqlalchemy.orm.exc import NoResultFound

from config import logger


""" Clothes Service

This module contains the Clothes Service class which is responsible
for handling all the business logic related to the Clothes model.

The clothes service is responsible for joining the colors to the clothes.

The ClothesService class contains the following methods:
    - get_user_clothes: get all clothes from a user
    - get_by_id: get clothes by id
    - get_all: get all clothes
    - create: create clothes
    - update: update clothes
    - delete: delete clothes
    - join_clothes_colors: join the colors to the clothes

@Author: Franklin Neves Filho
"""


class ClothesService(Service):
    def __init__(self, db):
        super().__init__(db)
        self.jwt = JwtService()

    def get_all_colors(self) -> Response:
        """
        Get all colors
        :return: {
            node: List[Color],
            errors: List[str]
        }
        """

        colors = self.db.query(Color).all()
        if not colors:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=colors)

    def get_all_styles(self) -> Response:
        """
        Get all styles
        :return: {
            node: List[Style],
            errors: List[str]
        }
        """
        styles = self.db.query(Style).all()
        if not styles:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=styles)

    def get_all_categories(self) -> Response:
        """
        Get all categories
        :return: {
            node: List[Category],
            errors: List[str]
        }
        """
        categories = self.db.query(Category).all()
        if not categories:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=categories)

    def get_all_patterns(self) -> Response:
        """
        Get all patterns
        :return: {
            node: List[Pattern],
            errors: List[str]
        }
        """
        patterns = self.db.query(Pattern).all()
        if not patterns:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=patterns)

    def get_all_fabrics(self) -> Response:
        """
        Get all fabrics
        :return: {
            node: List[Fabric],
            errors: List[str]
        }
        """
        fabrics = self.db.query(Fabric).all()
        if not fabrics:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=fabrics)

    def get_user_clothes(self, token: str) -> Response:
        """
        Get all clothes from a user
        :param token: str
        :return: {
            node: List[Clothes],
            errors: List[str]
        }
        """
        user_id = self.jwt.decode_token(token)['user_id']
        logger.info(f"User ID: {user_id}")

        if user_id is None:
            return ResponseFactory.generate_unauthorized_response()

        clothes = self.db.query(Clothes).filter(Clothes.user_id == user_id).all()
        logger.info(f"Clothes: {clothes}")
        return ResponseFactory.generate_ok_response(node=clothes)

    def get_by_id(self, item_id: int) -> Response:
        """
        Get clothes by id
        :param item_id: int
        :return: {
            node: Clothes,
            errors: List[str]
        }
        """
        clothes = self.db.query(Clothes).get(item_id)
        if clothes is None:
            return ResponseFactory.generate_not_found_response()
        return ResponseFactory.generate_ok_response(node=clothes)

    def get_all(self) -> Response:
        """
        Get all clothes
        :return: {
            node: List[Clothes],
            errors: List[str]
        }
        """
        clothes = self.db.query(Clothes).options(joinedload(Clothes.colors)).all()
        if not clothes:
            return ResponseFactory.generate_not_found_response()

        return ResponseFactory.generate_ok_response(node=clothes)

    def create(self, data: CreateClothes) -> Response:
        """
        Create a new clothes
        :param data: CreateClothes
        :return: {
            node: Clothes,
            errors: List[str]
        }
        """
        # Check if style exists
        style_exists = self.db.query(Style).filter(Style.name == data.style).first()
        if not style_exists:
            return ResponseFactory.generate_error_response(message="Style does not exist")

        # Check if category exists
        category_exists = self.db.query(Category).filter(Category.name == data.category).first()
        if not category_exists:
            return ResponseFactory.generate_error_response(message="Category does not exist")

        # Check if pattern exists
        pattern_exists = self.db.query(Pattern).filter(Pattern.name == data.pattern).first()
        if not pattern_exists:
            return ResponseFactory.generate_error_response(message="Pattern does not exist")

        # Check if fabric exists
        fabric_exists = self.db.query(Fabric).filter(Fabric.name == data.fabric).first()
        if not fabric_exists:
            return ResponseFactory.generate_error_response(message="Fabric does not exist")

        # Check if color exist
        color_exists = self.db.query(Color).filter(Color.name == data.color).first()
        if not color_exists:
            return ResponseFactory.generate_error_response(message="Color does not exist")

        # ensure that the clothes is not repeated
        clothes = self.db.query(Clothes).filter(Clothes.name == data.name).first()
        if clothes:
            return ResponseFactory.generate_error_response(message="Clothes already exists")

        # Create a new Clothes object
        clothes = Clothes(
            user_id=data.user_id,
            name=data.name,
            image_url=data.image_url,
            category=data.category,
            style=data.style,
            pattern=data.pattern,
            fabric=data.fabric,
            color=data.color
        )

        self.db.add(clothes)
        self.db.commit()

        return ResponseFactory.generate_created_response(node=clothes)

    def update(self, item_id: int, data: CreateClothes) -> Response:
        try:
            clothes = self.db.query(Clothes).filter(Clothes.id == item_id).one()
        except NoResultFound:
            return ResponseFactory.generate_not_found_response()

        # Update the Clothes object
        clothes.user_id = data.user_id
        clothes.image_url = data.image_url
        clothes.category = data.category
        clothes.style = data.style
        clothes.pattern = data.pattern
        clothes.fabric = data.fabric
        clothes.color = data.color

        self.db.commit()

        return ResponseFactory.generate_ok_response(node=clothes)

    def delete(self, item_id: int) -> Response:
        clothes = self.get_by_id(item_id)
        if clothes is None:
            return ResponseFactory.generate_not_found_response()

        outfits = self.db.query(Outfit).filter(Outfit.clothes.any(Clothes.id == item_id)).all()
        for outfit in outfits:
            self.db.query(Outfit).filter(Outfit.id == outfit.id).delete()

        self.db.query(Clothes).filter(Clothes.id == item_id).delete()
        self.db.commit()

        return ResponseFactory.generate_ok_response(node="Clothes deleted successfully")
