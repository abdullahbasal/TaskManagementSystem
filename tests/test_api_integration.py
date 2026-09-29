from app import app
from database.database import get_connection


def test_register_and_login():
    client = app.test_client()

    username = "integration_user"
    password = "123456"

    register_response = client.post(
        "/api/users/register",
        json={
            "username": username,
            "password": password
        }
    )

    assert register_response.status_code in [201, 409]

    login_response = client.post(
        "/api/users/login",
        json={
            "username": username,
            "password": password
        }
    )

    assert login_response.status_code == 200

    data = login_response.get_json()

    assert data["user"]["username"] == username


def test_create_and_get_task():
    client = app.test_client()

    username = "integration_task_user"
    password = "123456"

    client.post(
        "/api/users/register",
        json={
            "username": username,
            "password": password
        }
    )

    login_response = client.post(
        "/api/users/login",
        json={
            "username": username,
            "password": password
        }
    )

    user_id = login_response.get_json()["user"]["id"]

    create_response = client.post(
        f"/api/tasks/{user_id}",
        json={
            "title": "Integration Test Task",
            "description": "Testing API and database integration",
            "due_date": "2026-10-15"
        }
    )

    assert create_response.status_code == 201

    get_response = client.get(
        f"/api/tasks/{user_id}"
    )

    assert get_response.status_code == 200

    data = get_response.get_json()

    assert len(data["tasks"]) > 0


def test_update_and_delete_task():
    client = app.test_client()

    username = "integration_update_user"
    password = "123456"

    client.post(
        "/api/users/register",
        json={
            "username": username,
            "password": password
        }
    )

    login_response = client.post(
        "/api/users/login",
        json={
            "username": username,
            "password": password
        }
    )

    user_id = login_response.get_json()["user"]["id"]

    create_response = client.post(
        f"/api/tasks/{user_id}",
        json={
            "title": "Task Before Update",
            "description": "Original description",
            "due_date": "2026-10-15"
        }
    )

    task_id = create_response.get_json()["task_id"]

    update_response = client.put(
        f"/api/tasks/{user_id}/{task_id}",
        json={
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2026-10-20",
            "status": "Completed"
        }
    )

    assert update_response.status_code == 200

    get_response = client.get(
        f"/api/tasks/{user_id}/{task_id}"
    )

    task = get_response.get_json()["task"]

    assert task["title"] == "Updated Task"
    assert task["status"] == "Completed"

    delete_response = client.delete(
        f"/api/tasks/{user_id}/{task_id}"
    )

    assert delete_response.status_code == 200

    get_deleted_response = client.get(
        f"/api/tasks/{user_id}/{task_id}"
    )

    assert get_deleted_response.status_code == 404


def test_notification_integration():
    client = app.test_client()

    username = "integration_notification_user"
    password = "123456"

    client.post(
        "/api/users/register",
        json={
            "username": username,
            "password": password
        }
    )

    login_response = client.post(
        "/api/users/login",
        json={
            "username": username,
            "password": password
        }
    )

    user_id = login_response.get_json()["user"]["id"]

    response = client.get(
        f"/api/notifications/{user_id}"
    )

    assert response.status_code == 200

    data = response.get_json()

    assert "message" in data
    assert "count" in data
    assert "tasks" in data