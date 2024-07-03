class Singleton:
    _instances = {}

    def __new__(cls, *args, **kwargs) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instances[cls]
    

singleton_1 = Singleton()
singleton_2 = Singleton()

print(singleton_1 is singleton_2) # Return 'True'