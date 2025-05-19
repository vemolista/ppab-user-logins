from hashlib import sha256

from src.core.credentials import is_valid_credentials

username = input("Username: ")
password = input("Password: ")

hashed_pw = sha256(password.encode()).hexdigest()

if is_valid_credentials(username, hashed_pw):
    print("secret")
else:
    print("get lost, fool!")
