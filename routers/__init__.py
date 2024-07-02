from .main_router import MainRouter
from .user_router import UserRouter
from .clothes_router import ClothesRouter
from .outfit_router import OutfitRouter
from .auth_router import AuthRouter

routers = [
    MainRouter,
    UserRouter,
    ClothesRouter,
    OutfitRouter,
    AuthRouter
]


# This function will register all routers in the routers list
def register_routers(app, services):
    for router in routers:
        app.include_router(router(services).getRoutes())
