import jwt
from datetime import datetime, timedelta
from utils import KeyGeneratorUtil
from config import logger


class JwtService:

    def __init__(self):
        self.keys = KeyGeneratorUtil.generate_keys()
        self.private_key = self.keys['private_key']
        self.public_key = self.keys['public_key']
        self.algorithm = 'RS256'
        self.expire_time = 3600

    def generate_token(self, data: dict) -> str:
        """
        Generate a jwt token
        :param data: dictionary with the data to be encoded
        :return: jwt token
        """
        return jwt.encode(data, self.private_key, algorithm=self.algorithm)

    def isExpired(self, token: str) -> bool:
        """
        Check if a token is expired
        :param token: jwt token
        :return: True if the token is expired, False otherwise
        """
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return datetime.fromtimestamp(decoded['exp']) < datetime.now()
        except Exception as e:
            logger.error(f"Error decoding token: {e}")
            return True

    def decode_token(self, token: str) -> dict:
        """
        Verify and decode a jwt token
        :param token: jwt token
        :return: dictionary with the decoded data
        """
        try:
            return jwt.decode(token, self.public_key, algorithms=[self.algorithm])
        except Exception as e:
            logger.error(f"Error decoding token: {e}")
            return {}
