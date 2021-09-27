from flask import request, Blueprint
from flask import jsonify as jsonify_flask
from ..models import User
from ..decorators import login_required
from ..auth import encode_token
from ..google import is_valid_google_token

main = Blueprint("api", __name__)


TOKEN_LIVE_TIME_MINUTES = 60 * 24


def jsonify(data):
    return jsonify_flask(
        {"data": data}
    )


@main.route("/api/v1/send_message")
def send_message():
    data = request.json

    return "access denied"


@main.route("/api/v1/user")
def user():
    data = request.json

    return "user info"


@main.route("/api/v1/chats")
def chats():
    data = request.json


@main.route("/api/v1/users")
@login_required
def users():
    data = request.json
    search_value = data["search"]


@main.route("/api/v1/messages")
def messages():
    pass


@main.route("/api/v1/auth/login", methods=["POST"])
def auth_login():
    token = request.json["token"]

    valid_token_data = is_valid_google_token(token)

    if not valid_token_data:
        return jsonify({"message": "invalid google token"})

    encoded_token = encode_token(valid_token_data.id)

    return jsonify({
                "expire": TOKEN_LIVE_TIME_MINUTES * 60,
                "token": f"Bearer {encoded_token}",
                })
