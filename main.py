import sqlite3

from src.core.credentials import get_sha256_string, is_valid_credentials
from src.shell.user_repo import add_user, get_user_by_username

cx = sqlite3.connect("db/db.db")

action = int(input("One (1) for login, (2) for sign up: "))

if action == 1:
    username = input("Username: ")
    password = input("Password: ")

    hashed_pw = get_sha256_string(password)

    cur = cx.cursor()

    user = get_user_by_username(cur, username)

    if is_valid_credentials(user, hashed_pw):
        print("Logged in!")
    else:
        print("Incorrect username or password.")

elif action == 2:
    print("Creating a new user")
    username = input("Username: ")
    password = input("Password: ")

    hashed_pw = get_sha256_string(password)

    cur = cx.cursor()
    add_user(cur, username, hashed_pw)

    print("Success!")


else:
    print("Invalid input. Only 1 (for login) or 2 (for sign up) is allowed.")
