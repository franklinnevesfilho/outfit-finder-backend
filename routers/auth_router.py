from fastapi import APIRouter
from services import AuthService
from utils import Router
from models import LoginUser, CreateUser


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
            print("login_data", login_data)
            return auth_service.login(login_data)

        @router.post("/register")
        async def register(register_data: CreateUser):
            return auth_service.register(register_data)

        return router
