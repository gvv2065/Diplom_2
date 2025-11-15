from dataclasses import dataclass

@dataclass
class UserCreateRequest:
    email: str
    password: str
    name: str

@dataclass
class UserLoginRequest:
    email: str
    password: str
        