from flask import Blueprint, request
from components.user.user_service import register_user, login_user

user_routes = Blueprint("user_routes", __name__)


@user_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"message": "Username and password are required"}, 400

    if register_user(username, password):
        return {"message": "User registered successfully"}, 201

    return {"message": "Username already exists"}, 409


@user_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return {"message": "Username and password are required"}, 400

    user = login_user(username, password)

    if user:
        return {
            "message": "Login successful",
            "user": user
        }, 200

    return {"message": "Invalid username or password"}, 401