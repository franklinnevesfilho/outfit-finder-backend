from pydantic import BaseModel


class ClothesPredictionRequest(BaseModel):
    """ ClothesPredictionRequest

    This class is a Pydantic model that represents the request body for the
    clothes prediction endpoint.

    The request body consists of:
        - token: jwt token representing the user_id
        - usage: the usage for the outfit
        - weather: the weather for the outfit
        - season: the season for the outfit
    """

    token: str
    usage: str
    weather: str
    season: str
