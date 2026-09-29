from database.database import get_connection


def register_user(username, password):
    connection = get_connection()

    try:
        connection.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        connection.commit()
        return True
    except Exception:
        return False
    finally:
        connection.close()


def login_user(username, password):
    connection = get_connection()

    user = connection.execute(
        "SELECT id, username FROM users WHERE username = ? AND password = ?",
        (username, password)
    ).fetchone()

    connection.close()

    if user:
        return dict(user)

    return None