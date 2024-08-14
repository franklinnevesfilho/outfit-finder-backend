from franklin_fastapi_extension import DTO
import re

@DTO
class UserRegistration:
    email: str
    password: str
    first_name: str
    last_name: str

    VALIDATIONS = {
        "email": re.compile(r"[^@]+@[^@]+\.[^@]+"),
        "password": re.compile(r"[A-Za-z0-9@#$%^&+=]{8,}"),
        "first_name": re.compile(r"[A-Za-z]{2,}"),
        "last_name": re.compile(r"[A-Za-z]{2,}")
    }

@DTO
class UserLogin:
    email: str
    password: str

@DTO
class UserPasswordReset:
    user_id: str
    new_password: str
