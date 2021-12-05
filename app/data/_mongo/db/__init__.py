from pymongo import MongoClient

from app.config import MongoConfig

client = MongoClient(MongoConfig.base_config())
db = client[MongoConfig.DB_NAME]
