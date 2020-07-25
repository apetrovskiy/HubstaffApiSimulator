from fastapi import Depends, FastAPI, Header, HTTPException
from .routers.v1 import users

app = FastAPI()

app.include_router(users)
