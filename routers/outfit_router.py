from fastapi import APIRouter
from services import OutfitService
from utils import Router
from models import CreateOutfit


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

        @router.get("/user/{user_id}")
        async def get_user_outfits(user_id: int):
            return outfit_service.get_user_outfits(user_id)

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

        return router
