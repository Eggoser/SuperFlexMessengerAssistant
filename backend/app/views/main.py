from flask import request, jsonify, Blueprint
from ..google import request_get_user_google

main = Blueprint("api", __name__)


@main.route("/api/v1/send_message")
def send_message():
    pass


@main.route("/api/v1/messages")
def messages():
    pass


@main.route("/api/v1/auth/login", methods=["GET", "POST"])
def auth_login():
    print(request.json)
    print(request.method)
    print(request.cookies)

    return jsonify({"data": "hello world"})
