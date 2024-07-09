"""
This class is meant to take in a dictionary of data and return a JWT token
"""

from datetime import datetime, timedelta
import jwt
from utils.security.jwt_key_generator import KeyGeneratorUtil


class JwtFactory:

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
        data['exp'] = datetime.utcnow() + timedelta(seconds=self.expire_time)
        return jwt.encode(data, self.private_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> dict:
        """
        Decode a jwt token
        :param token:
        :return: dictionary with the decoded data
        """
        return jwt.decode(token, self.public_key, algorithms=[self.algorithm])
