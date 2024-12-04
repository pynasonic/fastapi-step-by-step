from pymongo import MongoClient
from app.config import settings


def get_database():
    client = MongoClient(settings.CFG['MONGO_DB_URL'])
    return client['todo_database']
