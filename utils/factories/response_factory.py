from .response import Response
from fastapi.responses import JSONResponse

status_codes = {
    'success': 200,
    'created': 201,
    'no_content': 204,
    'bad_request': 400,
    'unauthorized': 401,
    'forbidden': 403,
    'not_found': 404,
    'conflict': 409,
    'internal_server_error': 500
}


class ResponseFactory:

    @staticmethod
    def _generate_response(status: str, response: Response = None):
        return JSONResponse(
            content=response.dict(),
            status_code=status_codes[status]
        )

    @staticmethod
    def generate_error_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='bad_request')

    @staticmethod
    def generate_ok_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='success')

    @staticmethod
    def generate_created_response():
        return ResponseFactory._generate_response(status='created')

    @staticmethod
    def generate_bad_request_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='bad_request')

    @staticmethod
    def generate_unauthorized_response():
        return ResponseFactory._generate_response(status='unauthorized')

    @staticmethod
    def generate_forbidden_response():
        return ResponseFactory._generate_response(status='forbidden')

    @staticmethod
    def generate_not_found_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='not_found')

    @staticmethod
    def generate_conflict_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='conflict')

    @staticmethod
    def generate_internal_server_error_response(response: Response):
        return ResponseFactory._generate_response(response=response, status='internal_server_error')

    @staticmethod
    def generate_response(response: Response, status='success'):
        return ResponseFactory._generate_response(response=response, status=status)

    @staticmethod
    def generate_response_from_exception(exception):
        return ResponseFactory._generate_response(
            response=Response(errors=[str(exception)]), status='internal_server_error')

    @staticmethod
    def generate_no_content_response():
        return ResponseFactory._generate_response(status='no_content')


