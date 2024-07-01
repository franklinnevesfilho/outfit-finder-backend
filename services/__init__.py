from .user_service import UserService
from .clothes_service import ClothesService
from .outfit_service import OutfitService

services = {
    'user_service': UserService,
    'clothes_service': ClothesService,
    'outfit_service': OutfitService
}


def register_services(database):
    for service in services:
        services[service] = services[service](database)

    return services
