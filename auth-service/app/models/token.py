from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str
    algorithm: str
    expiration: int

class TokenData(BaseModel):
    user_id: str