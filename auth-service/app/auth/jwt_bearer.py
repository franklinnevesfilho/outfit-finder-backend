from fastapi import HTTPException, Request
from fastapi.openapi.models import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials
from app.handlers.jwt_handler import decodeJWT  # Assuming this is your JWT decoding function


class JwtBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JwtBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request) -> str:
        # Call the __call__ method of HTTPBearer directly
        credentials: HTTPAuthorizationCredentials = await super().__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme")

            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token")

            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization credentials")

    def verify_jwt(self, token: str) -> bool:
        is_token_valid: bool = False

        payload = decodeJWT(token)  # decodeJWT should return None if token is invalid

        if payload:
            is_token_valid = True

        return is_token_valid

    def __eq__(self, other):
        return isinstance(other, JwtBearer) and self.auto_error == other.auto_error

    def __hash__(self):
        return hash(self.auto_error)
