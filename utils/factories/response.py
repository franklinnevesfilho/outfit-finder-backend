"""Response model.

This model is used to create a response object that can be returned by the services.

"""


class Response:
    def __init__(self, node=None, errors=None, status=200):
        if errors is None:
            errors = []
        self.node = node
        self.errors = errors
        self.status = status

    def get_errors(self):
        return self.errors

    def get_node(self):
        return self.node

    def get_status(self):
        return self.status

    def to_dict(self):
        return {
            'node': self.node,
            'errors': self.errors,
            'status': self.status
        }

    def __repr__(self):
        return str(self.to_dict())
