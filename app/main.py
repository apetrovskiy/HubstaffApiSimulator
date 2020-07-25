from fastapi import FastAPI

from app.routers.v1 import users

app: FastAPI = FastAPI()

app.include_router(users.router)
