from utils import Service, Response, ResponseFactory
from .jwt_service import JwtService
from .ai_service import AIService
from models import User, CreateUser, ClothesPredictionRequest, Gender
from pydantic import BaseModel


"""
This module contains the User Service class which is responsible
for handling all the business logic related to the User model.

The UserService class implements the Service interface.

The UserService class contains the following methods:
    - get_by_id
    - get_all
    - create
    - update
    - delete
    - get_by_email

@Author: Franklin Neves Filho
"""


class UserResponse(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    gender: str


class UserService(Service):

    def __init__(self, db=None):
        super().__init__(db)
        self.jwt = JwtService()

    def get_by_id(self, item_id: int) -> Response:
        user = self.db.query(User).get(item_id)
        if user is None:
            return ResponseFactory.generate_not_found_response()
        return ResponseFactory.generate_ok_response(
            node=UserResponse(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                gender=user.gender
            ))

    def get_all(self) -> Response:
        users = self.db.query(User).all()
        user_response = [
            UserResponse(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                gender=user.gender
            )
            for user in users
        ]
        return ResponseFactory.generate_ok_response(node=user_response)

    def create(self, data: CreateUser) -> Response:
        try:
            user_found = self.db.query(User).filter(User.email == data.email)

            if user_found is not None:
                return ResponseFactory.generate_bad_request_response(errors=["User already exists"])

            user = User(**data.dict())
            self.db.add(user)
            self.db.commit()

            return ResponseFactory.generate_created_response(
            node=UserResponse(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                gender=user.gender
            ))
        except Exception as e:
            return ResponseFactory.generate_bad_request_response(errors=[str(e)])

    def update(self, token: str, data: CreateUser) -> Response:

        user_id = self.jwt.decode_token(token)['user_id']

        user = self.get_by_id(user_id)
        if user is None:
            return Response(errors=["User not found"], status=404)

        self.db.query(User).filter(User.id == user_id).update(data.model_dump())
        self.db.commit()
        return ResponseFactory.generate_ok_response(node="User updated successfully")

    def delete(self, token: str) -> Response:

        user_id = self.jwt.decode_token(token)['user_id']

        user = self.get_by_id(user_id)
        if user is None:
            return Response(errors=["User not found"], status=404)

        self.db.query(User).filter(User.id == user_id).delete()
        self.db.commit()
        return ResponseFactory.generate_ok_response(node="User deleted successfully")

    def get_by_email(self, email: str) -> Response:
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            return ResponseFactory.generate_not_found_response(errors=["User not found"])
        return ResponseFactory.generate_ok_response(
            node=UserResponse(
                id=user.id,
                email=user.email,
                first_name=user.first_name,
                last_name=user.last_name,
                gender=user.gender
            ))

    def get_gender(self) -> Response:
        genders = self.db.query(Gender).all()
        return ResponseFactory.generate_ok_response(node=genders)

    def get_predictions(self, predictionRequest: ClothesPredictionRequest):

        user_id = self.jwt.decode_token(predictionRequest.token)['user_id']
        user = self.db.query(User).get(user_id)
        if user is None:
            return ResponseFactory.generate_not_found_response(errors=["User not found"])

        prediction = AIService.predict(user, predictionRequest.usage, predictionRequest.season)

        return ResponseFactory.generate_ok_response(node=prediction)


