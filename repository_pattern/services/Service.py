from abc import ABC
from abc import abstractmethod

class Service(ABC):

    @abstractmethod
    def add(self):
        pass
    
    @abstractmethod
    def get_all(self):
        pass
