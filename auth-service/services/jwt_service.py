from franklin_fastapi_extension import Response
import jwt
import time
from logger import logger
from dto import Token
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend


_keys: dict = {
    "private": None,
    "public": None
}

_jwt_headers: dict = {
    "alg": "RS256",
    "typ": "JWT"
}


def generate_keys() -> dict | None:
    """
    Generate and store the RSA public and private keys.
    :return: dictionary containing the public and private keys
    """
    if _keys["private"] is None and _keys["public"] is None:
        try:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )

            _keys["private"] = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )

            public_key = private_key.public_key()

            _keys["public"] = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

            logger.info("Keys generated successfully")
            return _keys

        except Exception as e:
            logger.error(f"Error generating keys: {e}")
            return None

    else:
        logger.warning("Keys have already been generated")
        return _keys


def encode(payload: dict, headers: dict | None = None, claims: dict | None = None, expires_in: int = 3600) -> str | None:
    """
    Encode the payload into a JWT with an expiration time.
    :param payload: dictionary with the payload
    :param headers: optional dictionary with JWT headers
    :param claims: optional dictionary with standard claims like iss, sub, aud
    :param expires_in: expiration time in seconds (default is 3600 seconds, or 1 hour)
    :return: encoded JWT as a string or None if an error occurs
    """
    if _keys["private"] is None:
        logger.error("Private key not found")
        return None

    if headers is None:
        headers = _jwt_headers

    if claims is None:
        claims = {}

    # Set the expiration time
    payload["exp"] = time.time() + expires_in

    # Merge additional claims if provided
    payload.update(claims)

    try:
        token = jwt.encode(payload, _keys["private"], algorithm='RS256', headers=headers)
        logger.info("Token encoded successfully")
        return token
    except Exception as e:
        logger.error(f"Error encoding token: {e}")
        return None


def verify(token: str) -> dict | None:
    """
    Verify and decode the JWT token.
    :param token: string with the JWT token
    :return: dictionary with the decoded payload or None if verification fails
    """
    if _keys["public"] is None:
        logger.error("Public key not found")
        return None

    try:
        payload = jwt.decode(token, _keys["public"], algorithms=['RS256'])
        logger.info("Token verified successfully")
        return payload
    except jwt.ExpiredSignatureError:
        logger.error("Token has expired")
        return None
    except jwt.InvalidTokenError:
        logger.error("Invalid token")
        return None
    except Exception as e:
        logger.error(f"Error verifying token: {e}")
        return None

def refresh_token(refreshToken: Token) -> Response:
    """
    Refresh a JWT token by generating a new one with the same payload but a new expiration time.
    :param refreshToken: DTO with the token to refresh
    :return: string with the new token or None if an error occurs
    """
    if refreshToken.token is None:
        logger.error("Token not found")
        return Response(errors={"message": "Token not found"})

    payload = verify(refreshToken.token)
    if payload is None:
        logger.error("Invalid token")
        return Response(errors={"message": "Invalid token"})

    new_token = encode(payload)
    if new_token is None:
        logger.error("Error refreshing token")
        return Response(errors={"message": "Error refreshing token"})

    logger.info("Token refreshed successfully")
    return Response(node={"token": new_token})


def get_public_key() -> str | None:
    """
    Get the public key.
    :return: string with the public key or None if not found
    """
    if _keys["public"] is not None:
        logger.info("Public key retrieved successfully")
        return _keys["public"].decode("utf-8")  # Decoding from bytes to string for easier use
    else:
        logger.error("Public key not found")
        return None
