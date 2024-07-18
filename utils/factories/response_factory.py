from utils.interfaces.singleton_pattern import SingletonMeta
from .response import Response

status_codes = {
    'success': 200,
    'created': 201,
    'bad_request': 400,
    'unauthorized': 401,
    'forbidden': 403,
    'not_found': 404,
    'conflict': 409,
    'internal_server_error': 500
}


class ResponseFactory:

    @staticmethod
    def _generate_response(node=None, errors=None, status='success'):
        if errors is None:
            errors = []
        return Response(node=node, errors=errors, status=status_codes[status])

    @staticmethod
    def generate_error_response(message=None):
        return ResponseFactory._generate_response(errors=message, status='bad_request')

    @staticmethod
    def generate_ok_response(node=None):
        return ResponseFactory._generate_response(node=node, status='success')

    @staticmethod
    def generate_created_response(node=None):
        return ResponseFactory._generate_response(node=node, status='created')

    @staticmethod
    def generate_bad_request_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='bad_request')

    @staticmethod
    def generate_unauthorized_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='unauthorized')

    @staticmethod
    def generate_forbidden_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='forbidden')

    @staticmethod
    def generate_not_found_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='not_found')

    @staticmethod
    def generate_conflict_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='conflict')

    @staticmethod
    def generate_internal_server_error_response(errors=None):
        return ResponseFactory._generate_response(errors=errors, status='internal_server_error')

    @staticmethod
    def generate_response(node=None, errors=None, status='success'):
        return ResponseFactory._generate_response(node=node, errors=errors, status=status)

    @staticmethod
    def generate_response_from_exception(exception):
        return ResponseFactory._generate_response(errors=[str(exception)], status='internal_server_error')


