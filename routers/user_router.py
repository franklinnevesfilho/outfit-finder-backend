from fastapi import APIRouter
from services import UserService
from utils import Router
from models import CreateUser, LoginUser


""" User Router

This Router is responsible for handling the routes related to the User model.
This router uses the UserService to handle the business logic, and the
AuthService to handle the authentication logic.

The UserRouter contains the following methods:
    - get_all: get all users
    - get_by_email: get user by email
    - login: login user
    - create_user: create a new user
    
@Author: Franklin Neves Filho
"""


class UserRouter(Router):

    def __init__(self, services):
        super().__init__(services, "/users")

    def getRoutes(self):
        router = APIRouter(
            prefix=self.endpoint,
            tags=["user"]
        )
        user_service: UserService = self.getService("user_service")
        auth_service = self.getService("auth_service")

        @router.get("/")
        async def read_root():
            return {"Hello": "World"}

        @router.get("/login")
        async def login(login_data: LoginUser):
            print("login_data", login_data)
            return auth_service.login(login_data)

        @router.post("/register")
        async def create_user(user: CreateUser):
            return auth_service.register(user)

        @router.get("/all")
        async def get_all():
            return user_service.get_all()

        @router.get("/get/{user_email}")
        async def get_by_email(user_email: str):
            return user_service.get_by_email(user_email)

        return router

