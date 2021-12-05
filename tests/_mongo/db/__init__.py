from pymongo import MongoClient

from app.config import MongoConfig

client = MongoClient(MongoConfig.base_config())
db = client[f"{MongoConfig.DB_NAME}-test"]
