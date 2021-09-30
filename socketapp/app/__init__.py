import os
import pathlib
from dotenv import load_dotenv


base_dir = pathlib.Path(__file__).parent
load_dotenv(base_dir.parent / ".env")


secret_key = os.environ.get("SECRET_KEY")
print("SECRET KEY:", secret_key)

update_dictionary = {}
