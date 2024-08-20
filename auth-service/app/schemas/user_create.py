from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    id: int = Field(default=None)
    first_name: str = Field(default=None)
    last_name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        json_schema_extra = {
            "user_demo":{
                "firstName":"First Name",
                "lastName":"Last Name",
                "email":"user@email.com",
                "password":"password",
            }
        }