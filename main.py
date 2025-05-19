from src.core.credentials import is_valid_credentials

username = input("Username: ")
password = input("Password: ")


if is_valid_credentials(username, password):
    print("secret")
else:
    print("get lost, fool!")
