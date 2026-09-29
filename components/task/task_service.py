from database.database import get_connection
from datetime import datetime


def create_task(user_id, title, description, due_date):
    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tasks
        (user_id, title, description, due_date, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            user_id,
            title,
            description,
            due_date,
            "Pending",
            datetime.now().isoformat()
        )
    )

    connection.commit()
    task_id = cursor.lastrowid
    connection.close()

    return task_id


def get_tasks(user_id):
    connection = get_connection()

    tasks = connection.execute(
        """
        SELECT *
        FROM tasks
        WHERE user_id = ?
        ORDER BY id DESC
        """,
        (user_id,)
    ).fetchall()

    connection.close()

    return [dict(task) for task in tasks]


def get_task(task_id, user_id):
    connection = get_connection()

    task = connection.execute(
        """
        SELECT *
        FROM tasks
        WHERE id = ? AND user_id = ?
        """,
        (task_id, user_id)
    ).fetchone()

    connection.close()

    if task:
        return dict(task)

    return None


def update_task(task_id, user_id, title, description, due_date, status):
    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE tasks
        SET title = ?, description = ?, due_date = ?, status = ?
        WHERE id = ? AND user_id = ?
        """,
        (
            title,
            description,
            due_date,
            status,
            task_id,
            user_id
        )
    )

    connection.commit()
    updated = cursor.rowcount
    connection.close()

    return updated > 0


def delete_task(task_id, user_id):
    connection = get_connection()

    cursor = connection.execute(
        """
        DELETE FROM tasks
        WHERE id = ? AND user_id = ?
        """,
        (task_id, user_id)
    )

    connection.commit()
    deleted = cursor.rowcount
    connection.close()

    return deleted > 0