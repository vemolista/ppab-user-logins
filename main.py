import sqlite3
from hashlib import sha256

from src.core.credentials import is_valid_credentials

username = input("Username: ")
password = input("Password: ")

hashed_pw = sha256(password.encode()).hexdigest()

cx = sqlite3.connect("db/db.db")
cur = cx.cursor()

user = cur.execute(
    "select username, password_hash from users where username = (:username)",
    ({"username": username}),
).fetchone()

if is_valid_credentials(user, hashed_pw):
    print("secret")
else:
    print("get lost, fool!")
