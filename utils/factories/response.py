"""Response model.

This model is used to create a response object that can be returned by the services.

"""


class Response:
    def __init__(self, node=None, errors=None):
        if errors is None:
            errors = []
        self.node = node
        self.errors = errors

    def get_errors(self):
        return self.errors

    def get_node(self):
        return self.node

    def dict(self):
        return {
            'node': self.node,
            'errors': self.errors,
        }

    def __repr__(self):
        return str(self.dict())

