from utils import Service, Response, ResponseFactory
from models import User, CreateUser
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
        user_found = self.db.query(User).filter(User.email == data.email).first()

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

    def update(self, item_id: int, data: CreateUser) -> Response:
        user = self.get_by_id(item_id)
        if user is None:
            return Response(errors=["User not found"], status=404)

        self.db.query(User).filter(User.id == item_id).update(data.dict())
        self.db.commit()
        return ResponseFactory.generate_ok_response(node="User updated successfully")

    def delete(self, item_id: int) -> Response:
        user = self.get_by_id(item_id)
        if user is None:
            return Response(errors=["User not found"], status=404)

        self.db.query(User).filter(User.id == item_id).delete()
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

