from flask import jsonify, request
from .auth import decode_token
from .models import User
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        else:
            return jsonify({'message': 'a valid token is missing'})

        try:
            user_id = decode_token(token)
            current_user = User.query.filter_by(id=user_id).first_or_404()

            return f(current_user, *args,  **kwargs)
        except:
            return jsonify({'message': 'token is invalid'})

    return decorator
