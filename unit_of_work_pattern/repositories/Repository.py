from abc import ABC
from abc import abstractmethod

class AbstracRepository(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass
