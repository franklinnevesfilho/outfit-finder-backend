from fastapi import APIRouter
from services import UserService
from utils import Router
from models import CreateUser


class UserRouter(Router):

    def __init__(self, services):
        super().__init__(services, "/users")

    def getRoutes(self):
        router = APIRouter(
            prefix=self.endpoint,
            tags=["user"]
        )
        user_service: UserService = self.getService("user_service")

        @router.get(self.endpoint)
        async def read_root():
            return {"Hello": "World"}

        @router.post("/create")
        async def create_user(user: CreateUser):
            return user_service.create(user)

        @router.get("/all")
        async def get_all():
            return user_service.get_all()

        @router.get("/get/{user_email}")
        async def get_by_email(user_email: str):
            return user_service.get_by_email(user_email)

        return router

