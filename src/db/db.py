import os
from urllib.parse import quote_plus

from pymongo import MongoClient

USER = os.getenv("MONGO_INITDB_ROOT_USERNAME", "admin")
PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD", "adminadmin")
DB_HOST = os.getenv("DB_HOST", "mongodb")
DB_PORT = os.getenv("DB_PORT", 27017)

URI = "mongodb://%s:%s@%s:%s" % (
    quote_plus(USER),
    quote_plus(PASSWORD),
    DB_HOST,
    DB_PORT,
)

client = MongoClient(URI)
db = client[f"{DB_HOST}"]
