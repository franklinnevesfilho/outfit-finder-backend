from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

"""
This module is responsible for generating the public and private keys for the jwt service

This class also follows the singleton pattern

@Author: Franklin Neves
"""


class KeyGeneratorUtil:

    private_key = None
    public_key = None

    @staticmethod
    def generate_keys():
        """
        Generate the public and private keys
        :return: dictionary with the public and private keys
        """
        if KeyGeneratorUtil.private_key is None or KeyGeneratorUtil.public_key is None:
            private_key = rsa.generate_private_key(
                public_exponent=65537,
                key_size=2048,
                backend=default_backend()
            )
            public_key = private_key.public_key()

            KeyGeneratorUtil.private_key = private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            ).decode('utf-8')

            KeyGeneratorUtil.public_key = public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ).decode('utf-8')

        return {
            'private_key': KeyGeneratorUtil.private_key,
            'public_key': KeyGeneratorUtil.public_key
        }
