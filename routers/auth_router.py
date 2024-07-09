from fastapi import APIRouter
from services import AuthService
from utils import Router
from models import CreateUser, LoginUser

""" Auth Router

This Router is responsible for handling the routes related to the authentication of the user.
This router uses the AuthService to handle the business logic.

The AuthRouter contains the following methods:
    - login: login user
    - register: register user
    - reset_password: reset user password
   
@Author: Franklin Neves Filho 
"""


class AuthRouter(Router):
    def __init__(self, services):
        super().__init__(services, "/auth")

    def getRoutes(self):
        router = APIRouter(
            prefix=self.endpoint,
            tags=["auth"]
        )
        auth_service: AuthService = self.getService("auth_service")

        @router.post("/login")
        async def login(login_data: LoginUser):
            result = auth_service.login(login_data)
            print(result)
            return result

        @router.post("/register")
        async def register(user: CreateUser):
            return auth_service.register(user)

        @router.get("/reset-password/{token}")
        async def reset_password(token: str, email: str):
            return auth_service.reset_password(token, email)

        return router
