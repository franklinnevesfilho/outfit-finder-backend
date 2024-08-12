from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import jwt
from logger import logger


_keys: dict = {
    "private": None,
    "public": None
}


def generate_keys():
    """
    Generate the public and private keys
    :return: dictionary with the public and private keys
    """
    if _keys["private"] is None and _keys["public"] is None:
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

        return _keys
    else:
        logger.error("Keys already generated")
        return None


def encode(payload: dict) -> str | None:
    """
    Encode the payload
    :param payload: dictionary with the payload
    :return: encoded token
    """
    if _keys["private"] is None:
        logger.error("Private key not found")
        return None

    return jwt.encode(payload, _keys["private"], algorithm='RS256')


def decode(token: str) -> dict | None:
    """
    Decode the token
    :param token:
    :return: payload
    """

    if _keys["public"] is None:
        logger.error("Public key not found")
        return None

    return jwt.decode(token, _keys["public"], algorithms=['RS256'])
