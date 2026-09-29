import uuid

from components.user.user_service import register_user, login_user


def unique_username(prefix):
    return f"{prefix}_{uuid.uuid4().hex}"


def test_register_user():
    username = unique_username("test_register")
    password = "123456"

    result = register_user(username, password)

    assert result is True


def test_login_user():
    username = unique_username("test_login")
    password = "123456"

    register_user(username, password)

    user = login_user(username, password)

    assert user is not None
    assert user["username"] == username


def test_login_user_with_wrong_password():
    username = unique_username("wrong_password")
    password = "123456"

    register_user(username, password)

    user = login_user(username, "wrongpassword")

    assert user is None