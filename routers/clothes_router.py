from fastapi import APIRouter
from services import ClothesService
from utils import Router
from models import CreateClothes


class ClothesRouter(Router):

    def __init__(self, services):
        super().__init__(services, "/clothes")

    def getRoutes(self):
        router = APIRouter()
        clothes_service: ClothesService = self.getService("clothes_service")

        @router.get(self.endpoint)
        async def read_root():
            return {"Hello": "World"}

        @router.get(self.endpoint+"/user/{user_id}")
        async def get_user_clothes(user_id: int):
            return clothes_service.get_user_clothes(user_id)

        @router.post(f"{self.endpoint}/create")
        async def create_clothes(clothes: CreateClothes):
            return clothes_service.create(clothes)

        @router.get(f"{self.endpoint}/all")
        async def get_all():
            return clothes_service.get_all()

        @router.get(self.endpoint + "/get/{clothes_id}")
        async def get_by_id(clothes_id: int):
            return clothes_service.get_by_id(clothes_id)

        @router.delete(self.endpoint + "/delete/{clothes_id}")
        async def delete(clothes_id: int):
            return clothes_service.delete(clothes_id)

        @router.put(self.endpoint + "/update/{clothes_id}")
        async def update(clothes_id: int, clothes: CreateClothes):
            return clothes_service.update(clothes_id, clothes)

        return router
