from models.User import User
from repositories.unit_of_work import UnitOfWork

class UserService:
    def __init__(self, unit_of_work=UnitOfWork()) -> None:
        self.__unit_of_work = unit_of_work
        self.err = ""

    def add(self, user: User) -> None:
        if user.id != None:
            self.__unit_of_work.users.add(user)
        else:
            self.err = "ID required"

    def get_all(self) -> list[User]:
        return self.__unit_of_work.users.get_all()
    