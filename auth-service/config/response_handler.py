from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse
from typing import Any, Optional, List

# Assuming logger is defined in your .config module
from .config import logger

_status_codes = {
    200: "success",
    201: "created",
    204: "no content",
    400: "bad request",
    401: "unauthorized",
    403: "forbidden",
    404: "not found",
    405: "method not allowed",
    409: "conflict",
    422: "unprocessable entity",
    500: "internal server error",
    501: "not implemented",
    503: "service unavailable",
    504: "gateway timeout"
}


class Response(BaseModel):
    node: Optional[Any] = None
    errors: List[str] = []
    status: int

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.status not in _status_codes:
            raise ValueError(f"Invalid status code: {self.status}")
        logger.info(f"Response created with status: {self.status} - {_status_codes[self.status]}")


class JsonResponse(JSONResponse):

    def __init__(self, response: Response, status_code=200, **kwargs):
        super().__init__(content=response, status_code=response.get("status", status_code), **kwargs)

def validation_exception_handler(request, exc: RequestValidationError):
    """
    Custom exception handler for RequestValidationError.
    :param request: The request object.
    :param exc: The exception object.
    :return: JSONResponse
    """
    errors = []
    for error in exc.errors():
        errors.append(f'{error["loc"][0]}: {error["msg"]}')

    return JsonResponse(Response(node=None, errors=errors, status=422))