import sqlite3
from hashlib import sha256

from src.core.credentials import is_valid_credentials
from src.shell.user_repo import get_user_by_username

action = input("One (1) for sign up, (2) for login: ")

if action == 1:
    username = input("Username: ")
    password = input("Password: ")

    hashed_pw = sha256(password.encode()).hexdigest()

    cx = sqlite3.connect("db/db.db")
    cur = cx.cursor()

    user = get_user_by_username(cur, username)

    if is_valid_credentials(user, hashed_pw):
        print("secret")
    else:
        print("get lost, fool!")

elif action == 2:
    raise NotImplementedError()

elif action == 3:
    raise ValueError()
