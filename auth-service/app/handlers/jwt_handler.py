from config import config
import time
import jwt
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    return decodeJWT(token)

def _token_response(token: str):
    return {
        "access_token": token
    }

def signJWT(user_id: str):
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, config.JWT_SECRET, algorithm=config.JWT_ALGORITHM)
    return _token_response(token)


def decodeJWT(token: str):
    try:
        payload = jwt.decode(token, config.JWT_SECRET, algorithms=[config.JWT_ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return {
            "error": "Token expired"
        }
    except jwt.InvalidTokenError:
        return {
            "error": "Invalid token"
        }
    except Exception as e:
        return {
            "error": str(e)
        }
