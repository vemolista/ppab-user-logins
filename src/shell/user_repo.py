from src.core.data import User


def get_user_by_username(cursor, username) -> User | None:
    res = cursor.execute(
        "select username, password_hash from users where username = (:username)",
        ({"username": username}),
    ).fetchone()

    if res is None:
        return None

    return User(username=res[0], password_hash=res[1])


def add_user(cursor, username, hashed_password) -> User:
    cursor.execute(
        "insert into users (username, password_hash) values ((:username), (:password_hash))",
        ({"username": username, "password_hash": hashed_password}),
    )

    return get_user_by_username(cursor, username)
