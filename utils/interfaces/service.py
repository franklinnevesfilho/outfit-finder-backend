from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def get_by_id(self, item_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def update(self, item_id, data):
        pass

    @abstractmethod
    def delete(self, data):
        pass

