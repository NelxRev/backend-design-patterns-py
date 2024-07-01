from repositories.UserRepository import UserRepository
from services.UserService import UserService
from models.User import User

user_repository = UserRepository()
user_service = UserService(user_repository)

def main():
    while True:
        print("1. Add new user")
        print("2. List all users")
        print("3. Exit")
        print("==================")
        option = input("Select a option: \n")

        match option:
            case "1":
                id = int(input("Insert ID:"))
                fullname = input("insert FULLNAME:")
                email = input("Insert EMAIL:")
                new_user = User(id=id, fullname=fullname, email=email)
                user_service.add(new_user)
                print("User added")
            case "2":
                users = user_service.get_all()
                for user in users:
                    print(user)
            case "3":
                break
            case _:
                print("Invalid data")
        print("==================\n")

if __name__ == "__main__":
    main()           