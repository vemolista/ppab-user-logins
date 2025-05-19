import json
from hashlib import sha256

from src.core.credentials import is_valid_credentials

username = input("Username: ")
password = input("Password: ")

hashed_pw = sha256(password.encode()).hexdigest()

with open("config/credentials.json", "r") as f:
    data = f.read()

users = json.loads(data)

if is_valid_credentials(users, username, hashed_pw):
    print("secret")
else:
    print("get lost, fool!")
