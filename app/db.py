from pymongo import MongoClient

client = MongoClient("mongo", 27017)
db = client["student_db"]
students = db["students"]
