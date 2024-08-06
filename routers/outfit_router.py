
from fastapi import APIRouter
from services import OutfitService
from utils import Router
from models import CreateOutfit

""" Outfit Router

This Router is responsible for handling the routes related to the Outfit model.
This router uses the OutfitService to handle the business logic.

The OutfitRouter contains the following methods:
    - get_user_outfits: get all outfits from a user
    - create_outfit: create a new outfit
    - get_all: get all outfits
    - get_by_id: get outfit by id
    - delete: delete outfit by id
    - update: update outfit by id
    
@Author: Franklin Neves Filho
"""


class OutfitRouter(Router):

    def __init__(self, services):
        super().__init__(services, "/outfit")

    def getRoutes(self):
        router = APIRouter(
            prefix=self.endpoint,
            tags=["outfit"]
        )
        outfit_service: OutfitService = self.getService("outfit_service")

        @router.get("/")
        async def read_root():
            return {"Hello": "World"}

        @router.get("/user/{token}")
        async def get_user_outfits(token: str):
            return outfit_service.get_user_outfits(token)

        @router.post("/create")
        async def create_outfit(outfit: CreateOutfit):
            return outfit_service.create(outfit)

        @router.get("/all")
        async def get_all():
            return outfit_service.get_all()

        @router.get("/get/{outfit_id}")
        async def get_by_id(outfit_id: int):
            return outfit_service.get_by_id(outfit_id)

        @router.delete("/delete/{outfit_id}")
        async def delete(outfit_id: int):
            return outfit_service.delete(outfit_id)

        @router.put("/update/{outfit_id}")
        async def update(outfit_id: int, outfit: CreateOutfit):
            return outfit_service.update(outfit_id, outfit)

        @router.get("/usages")
        async def get_usages():
            return outfit_service.get_all_usages()

        @router.get("/weathers")
        async def get_weathers():
            return outfit_service.get_all_weathers()

        @router.get("/seasons")
        async def get_seasons():
            return outfit_service.get_all_seasons()

        return router
