from fastapi import APIRouter
from services import UserService, AIService
from models import ClothesPredictionRequest
from utils import Router


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

        @router.get("/")
        async def read_root():
            return {"Hello": "World"}

        @router.get("/all")
        async def get_all():
            return user_service.get_all()

        @router.post("/password-request")
        async def get_by_email(body: dict):
            print("body", body)
            email = body['email']
            return {"email": email}

        @router.get("/genders")
        async def get_gender():
            return user_service.get_gender()

        @router.post("/clothes-prediction")
        async def get_prediction(predictionRequest: ClothesPredictionRequest):
            return user_service.get_predictions(predictionRequest)

        return router

