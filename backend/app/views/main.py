from flask import request, Blueprint, jsonify
from ..decorators import login_required
from ..auth import encode_token
from ..google import is_valid_google_token


main = Blueprint("api", __name__)

TOKEN_LIVE_TIME_MINUTES = 60 * 24


@main.route("/v1/user")
@login_required
def get_user(current_user):
    return jsonify(current_user)


@main.route("/v1/auth/login", methods=["POST"])
def auth_login():
    token = request.json["token"]

    valid_token_data = is_valid_google_token(token)

    if not valid_token_data:
        return jsonify({"message": "invalid google token"})
    encoded_token = encode_token(str(valid_token_data["_id"]))

    return jsonify({
        "expire": TOKEN_LIVE_TIME_MINUTES * 60,
        "token": encoded_token,
    })
