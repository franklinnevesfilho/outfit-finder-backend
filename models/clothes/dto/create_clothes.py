from pydantic import BaseModel


class CreateClothes(BaseModel):
    user_id: int
    image_url: str
    category: str
    style: str
    pattern: str
    fabric: str
    colors: list[int]
