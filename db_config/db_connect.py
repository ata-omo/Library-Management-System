from pymongo import MongoClient
from urllib.parse import quote_plus
from fastapi import FastAPI

app = FastAPI()

# MongoDB Atlas credentials
username = "Dotenv"
password = "Lms@123"
cluster_name = "cluster0.gggagwc.mongodb.net"
database_name = "libmanager"

# Escape username and password
escaped_username = quote_plus(username)
escaped_password = quote_plus(password)

# Construct MongoDB URI
MONGO_URI = f"mongodb+srv://{escaped_username}:{escaped_password}@{cluster_name}/{database_name}?retryWrites=true&w=majority"

try:
    client = MongoClient(MONGO_URI)
    db = client[database_name]
    students_collection = db["students"]
except Exception as e:
    print("An error occurred:", e)