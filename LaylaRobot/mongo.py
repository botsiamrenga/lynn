import asyncio
import sys


from LaylaRobot import MONGO_DB_URI 
from pymongo import MongoClient

from LaylaRobot.conf import get_int_key, get_str_key


MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "DaisyX"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
db = client["LaylaRobot"]
