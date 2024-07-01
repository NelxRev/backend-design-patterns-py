class User:
    def __init__(self, id:int, fullname:str, email:str) -> None:
        self.id = id
        self.fullname = fullname
        self.email = email

    def __str__(self):
        return f"id: {self.id}, fullname: {self.fullname}, email: {self.email}"
