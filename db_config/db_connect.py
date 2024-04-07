from pymongo import MongoClient
from urllib.parse import quote_plus
from fastapi import FastAPI
from dotenv import load_dotenv
import os


app = FastAPI()

load_dotenv()


username = os.getenv("MONGO_USERNAME")
password = os.getenv("MONGO_PASSWORD")
cluster_name = os.getenv("MONGO_CLUSTER_NAME")
database_name = os.getenv("MONGO_DATABASE_NAME")


escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

MONGO_URI = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_name}/{database_name}?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)
    db = client[database_name]
    students_collection = db["students"]
except Exception as e:
    print("An error occurred:", e)