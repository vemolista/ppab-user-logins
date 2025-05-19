def get_user_by_username(cursor, username):
    return cursor.execute(
        "select username, password_hash from users where username = (:username)",
        ({"username": username}),
    ).fetchone()
