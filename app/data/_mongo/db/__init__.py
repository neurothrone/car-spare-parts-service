from pymongo import MongoClient

from app.config import MongoConfig
from app.settings import Settings

client = MongoClient(MongoConfig.base_config())

if Settings.TESTING:
    db = client[f"{MongoConfig.DB_NAME}-test"]
else:
    db = client[MongoConfig.DB_NAME]
