from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client["diet_db"]  # 使用你設定的 database 名稱
meals_collection = db["meals"]

def insert_meal(user_id: str, meal: str, content: str, calories: int):
    meals_collection.insert_one({
        "user_id": user_id,
        "meal": meal,
        "content": content,
        "calories": calories
    })
