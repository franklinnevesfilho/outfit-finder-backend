from utils import Service, Response, ResponseFactory, JwtFactory
from models import User, CreateUser, LoginUser

"""Auth Service

This service handles all the business logic related to the authentication of the user.

It uses the JwtService class to generate tokens and verify activities to the api

The AuthService class contains the following methods:
    - login: login the user
    - register: register the user
    - reset_password: reset the user password
    
@Author: Franklin Neves Filho
"""


class AuthService (Service):

    def __init__(self, db):
        super().__init__(db)
        self.jwt = JwtFactory()

    def login(self, data: LoginUser) -> Response:
        errorMsg = 'Invalid email or password'

        user = self.db.query(User).filter(User.email == data.email).first()
        if user is None:
            return ResponseFactory.generate_not_found_response(errors=[errorMsg])
        if user.password != data.password:
            return ResponseFactory.generate_bad_request_response(errors=[errorMsg])

        token = self.jwt.generate_token({'user_id': user.id})
        return ResponseFactory.generate_ok_response(node=token)

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

        token = self.jwt.generate_token({'user_id': user.id})
        return ResponseFactory.generate_ok_response(node=token)

    def reset_password(self, token: str, new_password: str) -> Response:
        user_id = self.jwt.decode_token(token)['user_id']
        user = self.db.query(User).get(user_id)
        user.password = new_password
        self.db.commit()
        return ResponseFactory.generate_ok_response()
