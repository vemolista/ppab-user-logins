def is_valid_credentials(users: dict[str], username: str, hashed_password: str) -> bool:
    actual_hashed_password = users.get(username, None)

    if actual_hashed_password is None:
        return False

    if hashed_password == actual_hashed_password:
        return True
