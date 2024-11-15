from pymongo import MongoClient
from bson import ObjectId
from config import Config

# MongoDB setup
client = MongoClient(Config.MONGO_URI)
db = client['mydatabase']
users_collection = db['users']

class UserModel:
    @staticmethod
    def find_by_username(username):
        return users_collection.find_one({'username': username})

    @staticmethod
    def find_by_id(user_id):
        return users_collection.find_one({'_id': ObjectId(user_id)})

    @staticmethod
    def create_user(username, hashed_password):
        user = {'username': username, 'password': hashed_password}
        return users_collection.insert_one(user)

    @staticmethod
    def serialize(user):
        user['_id'] = str(user['_id'])
        return user
