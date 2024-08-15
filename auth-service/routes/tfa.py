from franklin_fastapi_extension import POST
from logger import logger


@POST("/disable")
async def disable_2fa():
    logger.info("Disabling 2FA")
    return {"message": "2FA disabled successfully"}


@POST("/setup")
async def setup_2fa():
    logger.info("Setting up 2FA")
    return {"message": "2FA setup successfully"}


@POST("/verify")
async def verify_2fa():
    logger.info("Verifying 2FA")
    return {"message": "2FA verified successfully"}