from logger import logger
from services import jwt_service
from franklin_fastapi_extension import POST, GET, Query, request
from dto import Token

"""
Token management routes.

These routes are used to manage JWT tokens, including refreshing and revoking them.

The routes are protected by the JWT middleware, which verifies the token before allowing access.

The routes are:

- POST /refresh: Refresh a JWT token by generating a new one with the same payload but a new expiration time.
- POST /revoke: Revoke a JWT token, making it invalid for future requests.
- GET /token/public_key: Get the public key used to verify JWT tokens.
"""


@POST("/refresh")
async def refresh_token(query: Query):
    logger.info("Refreshing a token")
    return await request.call(jwt_service.refresh_token, query, Token)

@POST("/revoke")
async def revoke_token():
    logger.info("Revoking a token")
    # Logic to revoke the token
    return {"message": "Token revoked successfully"}

@GET("/token/public_key")
async def get_public_key():
    logger.info("Getting public key")
    return {"public_key": jwt_service.get_public_key()}
