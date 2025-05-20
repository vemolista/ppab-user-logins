# test credentials

from hashlib import sha256

from hypothesis import given
from hypothesis import strategies as st

from src.core.credentials import is_valid_credentials
from src.core.data import User


@given(st.builds(User), st.text())
def test_is_valid_credentials_random(user: User, hashed_pw):
    if user.password_hash == hashed_pw:
        assert is_valid_credentials(user, hashed_pw)
    else:
        assert not is_valid_credentials(user, hashed_pw)


def test_is_valid_credentials_success():
    pw_hashed = sha256("pw".encode()).hexdigest()

    user = User("john", pw_hashed)

    assert is_valid_credentials(user, pw_hashed)


def test_is_valid_credentials_fail():
    pw_hashed = sha256("pw".encode()).hexdigest()

    user = User("john", pw_hashed)

    assert not is_valid_credentials(user, "not_the_right_password_hash")
