from franklin_fastapi_extension import GET, POST
from logger import logger


@GET("/reset-request")
async def request_password_reset():
    logger.info("Requesting password reset")
    return {"message": "Password reset requested"}


@POST("/reset-confirm")
async def confirm_password_reset():
    logger.info("Confirming password reset")
    return {"message": "Password reset confirmed"}