from abc import ABC, abstractmethod
from repositories.user_repository import UserRepository

class UnitOfWork:
    def __init__(self):
        self.__user_repository = None

    @property
    def users(self):
        if self.__user_repository is None:
            self.__user_repository = UserRepository()
        return self.__user_repository
