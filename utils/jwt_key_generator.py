from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
import jwt
import datetime

"""
This module is responsible for generating the public and private keys for the jwt service
@Author: Franklin Neves
"""


class KeyGeneratorUtil:
    @staticmethod
    def generate_key() -> {}:
        """
        Generate a public and private key for the application.
        :return:
        {
            "public_key": "public_key
            "private_key": "private_key"
        }
        """
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        private_key_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

        public_key_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )

        return {
            "public_key": public_key_pem.decode(),
            "private_key": private_key_pem.decode()
        }
