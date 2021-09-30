import jwt
import datetime
from . import secret_key


def encode_token(payload, live_time_minutes=60 * 24):
    exp_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=live_time_minutes)
    return jwt.encode({'payload': payload,
                       'exp': exp_time},
                      secret_key, algorithm="HS256")


def decode_token(token):
    return jwt.decode(token, secret_key, algorithms=["HS256"])["payload"]
