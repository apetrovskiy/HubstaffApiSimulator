from fastapi import FastAPI

from .routers.v1 import users

app = FastAPI()

app.include_router(users.router)
