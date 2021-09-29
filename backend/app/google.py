import dotenv
import os
import json
import requests
from . import base_dir
from . import mongo

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

        existing_user = list(mongo["chat_levkovo"].users.find({"googleId": google_user["localId"]}))
        # existing_user = User.query.filter_by(googleId=google_user["localId"]).first()

        if existing_user:
            return existing_user[0]

        user = {
            "name": google_user["displayName"],
            "email": google_user["email"],
            "googleId": google_user["localId"],
            "avatarUrl": google_user["photoUrl"]
        }

        mongo["chat_levkovo"].users.insert_one(user)

        return user

    return False
