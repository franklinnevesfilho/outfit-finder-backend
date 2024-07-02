from fastapi import APIRouter
from utils import Router, Service


class MainRouter(Router):
    def __init__(self, services: dict):
        super().__init__(services)

    def getRoutes(self):
        router = APIRouter(
            tags=["main"]
        )

        @router.get(self.endpoint)
        async def read_root():
            return {"Hello": "World"}

        return router
