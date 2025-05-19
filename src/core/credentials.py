def is_valid_credentials(user: tuple[str, str], hashed_password: str) -> bool:
    if user is None:
        return False

    _, actual_hashed_password = user

    if hashed_password == actual_hashed_password:
        return True
