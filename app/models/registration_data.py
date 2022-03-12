from dataclasses import dataclass


@dataclass
class RegistrationData:
    password: str
    login: str
    tamagochi_name: str
    tamagochi_gender: str
