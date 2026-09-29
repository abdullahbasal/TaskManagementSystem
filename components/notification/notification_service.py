from database.database import get_connection
from datetime import datetime, timedelta


def get_upcoming_tasks(user_id):
    connection = get_connection()

    today = datetime.now().date()
    limit_date = today + timedelta(days=3)

    tasks = connection.execute(
        """
        SELECT id, title, due_date, status
        FROM tasks
        WHERE user_id = ?
        AND status = 'Pending'
        AND due_date != ''
        AND date(due_date) BETWEEN date(?) AND date(?)
        ORDER BY due_date ASC
        """,
        (
            user_id,
            today.isoformat(),
            limit_date.isoformat()
        )
    ).fetchall()

    connection.close()

    return [dict(task) for task in tasks]


def get_notification(user_id):
    tasks = get_upcoming_tasks(user_id)

    if not tasks:
        return {
            "message": "You have no upcoming tasks.",
            "count": 0,
            "tasks": []
        }

    return {
        "message": f"You have {len(tasks)} upcoming task(s).",
        "count": len(tasks),
        "tasks": tasks
    }