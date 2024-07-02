from utils import Service, Response, ResponseFactory
from models import User, CreateUser, LoginUser

"""Auth Service

This service handles all the business logic related to the authentication of the user.

It uses the JwtService class to generate tokens and verify activities to the api

The AuthService class contains the following methods:
    - login: login the user
    - register: register the user
    - get_by_email: get user by email
    -reset_password: reset the user password
    -logout: logout the user
    
@Author: Franklin Neves Filho
"""


class AuthService (Service):

    def __init__(self, db):
        super().__init__(db)

    def login(self, data: LoginUser) -> Response:
        user = self.db.query(User).filter(User.email == data.email).first()
        if user is None:
            return ResponseFactory.generate_not_found_response(errors=["There is no account with this email"])
        if user.password != data.password:
            return ResponseFactory.generate_bad_request_response()
        return ResponseFactory.generate_ok_response(node=user.id)

    def register(self, data: CreateUser) -> Response:
        user = self.db.query(User).filter(User.email == data.email).first()
        if user is not None:
            return ResponseFactory.generate_bad_request_response(errors=["User already exists"])

        user = User(
            email=data.email,
            first_name=data.first_name,
            last_name=data.last_name,
            password=data.password,
            gender=data.gender
        )
        self.db.add(user)
        self.db.commit()

        return ResponseFactory.generate_ok_response(node=user.id)

    def get_by_email(self, email: str) -> Response:
        user = self.db.query(User).filter(User.email == email).first()
        if user is None:
            return ResponseFactory.generate_not_found_response()
        return ResponseFactory.generate_ok_response(node=user.id)
