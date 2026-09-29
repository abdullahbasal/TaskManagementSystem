import uuid

from components.user.user_service import register_user, login_user
from components.task.task_service import (
    create_task,
    get_task,
    update_task,
    delete_task
)


def unique_username(prefix):
    return f"{prefix}_{uuid.uuid4().hex}"


def create_test_user():
    username = unique_username("white_box_user")
    password = "123456"

    register_user(username, password)

    user = login_user(username, password)

    return user["id"]


def test_register_existing_user():
    username = unique_username("existing_white_box_user")
    password = "123456"

    first_result = register_user(username, password)
    second_result = register_user(username, password)

    assert first_result is True
    assert second_result is False


def test_login_invalid_user():
    username = unique_username("non_existing_white_box_user")

    user = login_user(
        username,
        "123456"
    )

    assert user is None


def test_create_task_and_get_task():
    user_id = create_test_user()

    task_id = create_task(
        user_id,
        "White Box Task",
        "Testing task creation",
        "2026-10-15"
    )

    task = get_task(task_id, user_id)

    assert task is not None
    assert task["title"] == "White Box Task"


def test_update_non_existing_task():
    user_id = create_test_user()

    result = update_task(
        999999,
        user_id,
        "Updated Task",
        "Description",
        "2026-10-20",
        "Completed"
    )

    assert result is False


def test_delete_non_existing_task():
    user_id = create_test_user()

    result = delete_task(
        999999,
        user_id
    )

    assert result is False