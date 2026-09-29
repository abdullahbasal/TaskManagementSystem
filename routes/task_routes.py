from flask import Blueprint, request
from components.task.task_service import (
    create_task,
    get_tasks,
    get_task,
    update_task,
    delete_task
)

task_routes = Blueprint("task_routes", __name__)


@task_routes.route("/<int:user_id>", methods=["POST"])
def create(user_id):
    data = request.get_json()

    title = data.get("title")
    description = data.get("description", "")
    due_date = data.get("due_date", "")

    if not title:
        return {"message": "Title is required"}, 400

    task_id = create_task(
        user_id,
        title,
        description,
        due_date
    )

    return {
        "message": "Task created successfully",
        "task_id": task_id
    }, 201


@task_routes.route("/<int:user_id>", methods=["GET"])
def get_all(user_id):
    tasks = get_tasks(user_id)

    return {
        "tasks": tasks
    }, 200


@task_routes.route("/<int:user_id>/<int:task_id>", methods=["GET"])
def get_one(user_id, task_id):
    task = get_task(task_id, user_id)

    if not task:
        return {"message": "Task not found"}, 404

    return {
        "task": task
    }, 200


@task_routes.route("/<int:user_id>/<int:task_id>", methods=["PUT"])
def update(user_id, task_id):
    data = request.get_json()

    title = data.get("title")
    description = data.get("description", "")
    due_date = data.get("due_date", "")
    status = data.get("status", "Pending")

    if not title:
        return {"message": "Title is required"}, 400

    updated = update_task(
        task_id,
        user_id,
        title,
        description,
        due_date,
        status
    )

    if not updated:
        return {"message": "Task not found"}, 404

    return {
        "message": "Task updated successfully"
    }, 200


@task_routes.route("/<int:user_id>/<int:task_id>", methods=["DELETE"])
def delete(user_id, task_id):
    deleted = delete_task(task_id, user_id)

    if not deleted:
        return {"message": "Task not found"}, 404

    return {
        "message": "Task deleted successfully"
    }, 200