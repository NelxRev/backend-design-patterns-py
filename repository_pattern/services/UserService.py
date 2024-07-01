from models.User import User
from services.Service import Service
from repositories.UserRepository import UserRepository

class UserService(Service):
    def __init__(self, user_repository: UserRepository) -> None:
        self.__user_repository = user_repository
        self.err = ""

    def add(self, user: User) -> None:
        if user.id != None:
            self.__user_repository.add(user)
        else:
            self.err = "ID required"

    def get_all(self) -> list[User]:
        return self.__user_repository.get_all()
    