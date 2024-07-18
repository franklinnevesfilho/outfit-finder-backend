from .user_service import UserService
from .clothes_service import ClothesService
from .outfit_service import OutfitService
from .auth_service import AuthService
from .ai_service import AIService


services = {
    'user_service': UserService,
    'clothes_service': ClothesService,
    'outfit_service': OutfitService,
    'auth_service': AuthService,
    'ai_service': AIService

}


def register_services(database, s3):
    for service in services:
        if service == 'ai_service':
            services[service] = services[service](s3)
        else:
            services[service] = services[service](database)

    return services
