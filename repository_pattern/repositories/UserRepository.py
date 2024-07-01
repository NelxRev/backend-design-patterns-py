from repositories.Repository import AbstracRepository
from models.User import User

class UserRepository(AbstracRepository):
    def __init__(self):
        self.__users: list[User] = []
    
    def add(self, user: User) -> None:
        self.__users.append(user)

    def get_all(self) -> list[User]:
        return self.__users
