import os
import pathlib
import asyncio
from collections import defaultdict
import motor.motor_asyncio
from dotenv import load_dotenv


base_dir = pathlib.Path(__file__).parent
load_dotenv(base_dir.parent / ".env")


secret_key = os.environ.get("SECRET_KEY")
max_neg_value = float(os.environ.get("MAX_NEG_VALUE"))
debug = os.environ.get("DEBUG")
mongo = motor.motor_asyncio.AsyncIOMotorClient(os.environ.get("MONGO_URI"))

print("SECRET KEY:", secret_key)

triggers_dict = {}


class HookDictObj:
    def __init__(self, bind_to=None):
        self._data = False
        self.callbacks = {}
        self.callback_max_index = 0
        if bind_to:
            self.new_callback(bind_to)

    @property
    def value(self):
        return self._data

    @value.setter
    def value(self, val):
        self._data = val
        for index, item in self.callbacks.items():
            func, kwargs = item
            asyncio.get_event_loop().create_task(func(**kwargs, as_id=index))

    def new_callback(self, func, **kwargs):
        self.callbacks[self.callback_max_index] = (func, kwargs)
        self.callback_max_index += 1


update_dictionary = defaultdict(HookDictObj)
