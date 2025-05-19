users = {"hi": "ho"}


def is_valid_credentials(username: str, password: str) -> bool:
    actual_password = users.get(username, None)

    if actual_password is None:
        return False

    if password == actual_password:
        return True
