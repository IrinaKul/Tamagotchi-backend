from dataclasses import dataclass


@dataclass
class UpdatePasswordData:
    old_password: str
    new_password: str
