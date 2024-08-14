from franklin_fastapi_extension import Response
from dto import *
from logger import logger


def register_user(user: UserRegistration) -> Response:
    logger.info("Registering a new user")
    return Response(node=user, errors=None)


def login_user(user: UserLogin) -> Response:
    logger.info("Logging in a user")
    return Response(node=user, errors=None)

def confirm_password_reset(user: UserPasswordReset) -> Response:
    logger.info("Confirming password reset")
    return Response(node=user, errors=None)