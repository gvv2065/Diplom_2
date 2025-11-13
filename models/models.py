from dataclasses import dataclass

@dataclass
class UserCreateRequest:
    email: str
    password: str
    name: str
    