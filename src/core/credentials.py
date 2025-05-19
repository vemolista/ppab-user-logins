from src.core.data import User


def is_valid_credentials(user: User | None, hashed_password: str) -> bool:
    if user is None:
        return False

    if hashed_password == user.password_hash:
        return True
