import dotenv
import os
import json
import requests
from . import base_dir
from .models import User, db

dotenv.load_dotenv(base_dir.parent / ".env")


def is_valid_google_token(auth_token):
    api_key = os.environ.get("FIREBASE_API_KEY")
    request_url = os.environ.get("FIREBASE_REQUEST_USER_URL").format(api_key)

    google_data = requests.post(
        request_url,
        data=json.dumps({
            "idToken": auth_token
        }),
        headers={
            "content-type": "application/json",
        }
    ).json()

    if google_data.get("users") and len(google_data["users"]) == 1:
        google_user = google_data["users"][0]

        user = User(name=google_user["displayName"],
                    email=google_user["email"],
                    googleId=google_user["localId"],
                    avatarUrl=google_user["photoUrl"])

        db.session.add(user)
        try:
            db.session.commit()
        # пользователь существует
        except:
            print("user exist")
            pass

        return user

    return False


# вызывается, когда текущий токен в бд расходится с полученным
def update_user_google(data):
    pass


