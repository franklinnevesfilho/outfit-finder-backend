from typing import Type
from utils.factories.response_factory import ResponseFactory
from .service import Service
from abc import ABC, abstractmethod


class Router(ABC):

    def __init__(self, services, endpoint: str = "/"):
        self.services = services
        self.endpoint = endpoint

    @abstractmethod
    def getRoutes(self):
        pass

    def getService(self, service_name: str):
        return self.services[service_name]

