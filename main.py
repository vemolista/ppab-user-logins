username = input("Username: ")
password = input("Password: ")


actual_username = "hi"
actual_password = "ho"


def print_secret(username: str, password: str) -> bool:
    if username == actual_username and password == actual_password:
        return True


if print_secret(username, password):
    print("secret")
else:
    print("get lost, fool!")
