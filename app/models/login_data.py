from dataclasses import dataclass


@dataclass
class LoginData:
    name: str
    password: str
