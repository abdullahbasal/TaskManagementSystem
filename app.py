from flask import Flask
from flask_cors import CORS
from database.database import init_database
from routes.user_routes import user_routes
from routes.task_routes import task_routes
from routes.notification_routes import notification_routes

app = Flask(__name__)
CORS(app)

init_database()

app.register_blueprint(user_routes, url_prefix="/api/users")
app.register_blueprint(task_routes, url_prefix="/api/tasks")
app.register_blueprint(
    notification_routes,
    url_prefix="/api/notifications"
)


@app.route("/")
def home():
    return {"message": "Task Management System API is running"}


if __name__ == "__main__":
    app.run(debug=True)