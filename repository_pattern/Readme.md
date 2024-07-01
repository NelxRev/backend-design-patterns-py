# REPOSITORY PATTERN | PORT & ADAPTERS ARCHITECTURE

Example project approaches the design pattern using python, creating a local data persistence (user model list as in memory repository) and a basic menu as an interface. In addition, the hexagonal architecture was applied.
[Check more examples in repository](https://github.com/NelxRev/backend-design-patterns-py.git)

```
hexagonal_architecture/
├── models/
│   ├── user.py
├── repositories/
│   ├── abstract_repository.py
│   ├── user_repository.py
├── services/
│   ├── user_service.py
└── main.py

```

## Run

```
python main.py
```
```
python3 main.py
```