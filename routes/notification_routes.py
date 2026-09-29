from flask import Blueprint
from components.notification.notification_service import get_notification

notification_routes = Blueprint(
    "notification_routes",
    __name__
)


@notification_routes.route("/<int:user_id>", methods=["GET"])
def notification(user_id):
    return get_notification(user_id), 200