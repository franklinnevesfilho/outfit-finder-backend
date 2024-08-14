from franklin_fastapi_extension import POST, GET, request, Query
from services import auth_service, jwt_service
from dto import UserRegistration, UserLogin, UserPasswordReset
from logger import logger


@POST("/register")
async def register_user(user: Query):
    logger.info("Registering a user")
    return await request.call(auth_service.register_user, user, UserRegistration)


@POST("/login")
async def login_user(user: Query):
    logger.info("Logging in a user")
    return await request.call(auth_service.login_user, user, UserLogin)

@POST("/password-reset/request")
async def request_password_reset(query: Query):
    payload = jwt_service.verify(query.headers.get("Authorization"))
    return {"message": payload}

@GET("/password-reset/confirm")
async def confirm_password_reset(reset_password: Query):
    logger.info("Confirming password reset")
    return await request.call(auth_service.confirm_password_reset, reset_password, UserPasswordReset)


@POST("/social/{provider}/login")
async def social_login(provider: str):
    logger.info(f"Logging in with {provider}")
    return {"message": f"Logged in with {provider}"}

@POST("/2fa/setup")
async def setup_2fa():
    logger.info("Setting up 2FA")
    return {"message": "2FA setup successfully"}

@POST("/2fa/verify")
async def verify_2fa():
    logger.info("Verifying 2FA")
    return {"message": "2FA verified successfully"}

@POST("/2fa/disable")
async def disable_2fa():
    logger.info("Disabling 2FA")
    return {"message": "2FA disabled successfully"}