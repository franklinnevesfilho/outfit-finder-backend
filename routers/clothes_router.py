from fastapi import APIRouter
from services import ClothesService
from utils import Router
from models import CreateClothes

""" Clothes Router

This Router is responsible for handling the routes related to the Clothes model.
This router uses the ClothesService to handle the business logic.

The ClothesRouter contains the following methods:
    - get_user_clothes: get all clothes from a user
    - create_clothes: create a new clothes
    - get_all: get all clothes
    - get_by_id: get clothes by id
    - delete: delete clothes by id
    - update: update clothes by id

@Author: Franklin Neves Filho
"""


class ClothesRouter(Router):

    def __init__(self, services):
        super().__init__(services, "/clothes")

    def getRoutes(self):
        router = APIRouter(
            prefix=self.endpoint,
            tags=["clothes"]
        )
        clothes_service: ClothesService = self.getService("clothes_service")

        @router.get("/")
        async def read_root():
            return {"Hello": "World"}

        @router.get("/{token}")
        async def get_user_clothes(token: str):
            return clothes_service.get_user_clothes(token)

        @router.post("/create")
        async def create_clothes(clothes: CreateClothes):
            return clothes_service.create(clothes)

        @router.get("/all")
        async def get_all():
            return clothes_service.get_all()

        @router.get("/get/{clothes_id}")
        async def get_by_id(clothes_id: int):
            return clothes_service.get_by_id(clothes_id)

        @router.delete("/delete/{clothes_id}")
        async def delete(clothes_id: int):
            return clothes_service.delete(clothes_id)

        @router.put("/update/{clothes_id}")
        async def update(clothes_id: int, clothes: CreateClothes):
            return clothes_service.update(clothes_id, clothes)

        return router
