from fastapi import FastAPI
from routes.student_routes import std

app = FastAPI()

app.include_router(std)