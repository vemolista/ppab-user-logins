username = input("Username: ")
password = input("Password: ")


actual_username = "hi"
actual_password = "ho"


def is_valid_credentials(username: str, password: str) -> bool:
    if username == actual_username and password == actual_password:
        return True


if is_valid_credentials(username, password):
    print("secret")
else:
    print("get lost, fool!")
