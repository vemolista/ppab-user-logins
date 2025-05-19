from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    username: str
    password_hash: str
