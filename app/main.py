from fastapi import FastAPI

from app.routers.v1 import users
# from routers.v1 import users

app1: FastAPI = FastAPI()

app1.include_router(users.router)
