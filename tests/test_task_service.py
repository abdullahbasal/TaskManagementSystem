from components.user.user_service import register_user, login_user
from components.task.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task
)


def create_test_user():
    username = "task_test_user"
    password = "123456"

    register_user(username, password)

    user = login_user(username, password)

    return user["id"]


def test_create_task():
    user_id = create_test_user()

    task_id = create_task(
        user_id,
        "Test Task",
        "Test Description",
        "2026-10-15"
    )

    assert task_id is not None


def test_get_tasks():
    user_id = create_test_user()

    create_task(
        user_id,
        "Task List Test",
        "Description",
        "2026-10-15"
    )

    tasks = get_tasks(user_id)

    assert len(tasks) > 0
    assert tasks[0]["title"] == "Task List Test"


def test_get_task():
    user_id = create_test_user()

    task_id = create_task(
        user_id,
        "Single Task",
        "Description",
        "2026-10-15"
    )

    task = get_task(task_id, user_id)

    assert task is not None
    assert task["title"] == "Single Task"


def test_update_task():
    user_id = create_test_user()

    task_id = create_task(
        user_id,
        "Old Title",
        "Old Description",
        "2026-10-15"
    )

    result = update_task(
        task_id,
        user_id,
        "New Title",
        "New Description",
        "2026-10-20",
        "Completed"
    )

    assert result is True

    task = get_task(task_id, user_id)

    assert task["title"] == "New Title"
    assert task["status"] == "Completed"


def test_delete_task():
    user_id = create_test_user()

    task_id = create_task(
        user_id,
        "Delete Test",
        "Description",
        "2026-10-15"
    )

    result = delete_task(task_id, user_id)

    assert result is True

    task = get_task(task_id, user_id)

    assert task is None