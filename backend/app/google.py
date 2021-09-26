import dotenv
import os
import json
import requests
from . import base_dir

dotenv.load_dotenv(base_dir.parent / ".env")

template = """CI22yQEIorbJAQjEtskBCKmdygEIjtHKAQiMnssBCO/yywEItPjLAQie+csBCPj5ywEIx/3LAQii/ssBCL3+ywEIn//LAQ=="""


def request_get_user_google(auth_token):
    api_key = os.environ.get("FIREBASE_API_KEY")
    request_url = os.environ.get("FIREBASE_REQUEST_USER_URL").format(api_key)

    data = requests.post(
        request_url,
        data=json.dumps({
            "idToken": api_key
        }),
        headers={
            "Content-Type": "application/json",
            "x-client-data": template
        }
    ).text

    return data
