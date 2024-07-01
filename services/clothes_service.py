from sqlalchemy.orm import Session, joinedload
from models import Clothes, CreateClothes, Category, Style, Pattern, Fabric, Color
from utils import Service, Response, ResponseFactory
from typing import Type
from sqlalchemy.orm.exc import NoResultFound


class ClothesService(Service):
    def __init__(self, db: Session):
        self.db = db

    def get_user_clothes(self, user_id: int) -> Response:
        clothes = self.db.query(Clothes).filter(Clothes.user_id == user_id).all()
        clothes_response = [self.join_clothes_colors(cloth) for cloth in clothes]
        return ResponseFactory.generate_ok_response(node=clothes_response)

    def get_by_id(self, item_id: int) -> Response:
        clothes = self.db.query(Clothes).get(item_id)
        if clothes is None:
            return ResponseFactory.generate_not_found_response()
        clothes = self.join_clothes_colors(clothes)
        return ResponseFactory.generate_ok_response(node=clothes)

    def get_all(self) -> Response:
        clothes = self.db.query(Clothes).options(joinedload(Clothes.colors)).all()
        if not clothes:
            return ResponseFactory.generate_not_found_response()

        clothes = [self.join_clothes_colors(cloth) for cloth in clothes]

        return ResponseFactory.generate_ok_response(node=clothes)

    def create(self, data: CreateClothes) -> Response:
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

        # Check if colors exist
        colors = []
        for color in data.colors:
            color_exists = self.db.query(Color).filter(Color.id == color).first()
            if not color_exists:
                return ResponseFactory.generate_error_response(message="Color does not exist")
            colors.append(color_exists)

        clothes = Clothes(**data.dict())
        clothes.colors = colors

        self.db.add(clothes)
        self.db.commit()

        return ResponseFactory.generate_created_response(node=clothes)

    def update(self, item_id: int, data: CreateClothes) -> Response:
        try:
            clothes = self.db.query(Clothes).filter(Clothes.id == item_id).one()
        except NoResultFound:
            return ResponseFactory.generate_not_found_response()

        # Fetch the Color objects based on the provided color IDs
        color_objects = self.db.query(Color).filter(Color.id.in_(data.colors)).all()
        if len(color_objects) != len(data.colors):
            return ResponseFactory.generate_error_response(message="Some colors do not exist")

        # Update the Clothes object
        clothes.user_id = data.user_id
        clothes.image_url = data.image_url
        clothes.category = data.category
        clothes.style = data.style
        clothes.pattern = data.pattern
        clothes.fabric = data.fabric
        clothes.colors = color_objects  # Set with Color objects

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

    @staticmethod
    def join_clothes_colors(clothes: Type[Clothes]):
        return {
            "id": clothes.id,
            "user_id": clothes.user_id,
            "image_url": clothes.image_url,
            "category": clothes.category,
            "style": clothes.style,
            "pattern": clothes.pattern,
            "fabric": clothes.fabric,
            "colors": [color.name for color in clothes.colors]
        }
