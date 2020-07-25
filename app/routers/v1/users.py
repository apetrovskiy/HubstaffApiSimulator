from app.common.v1.urls import USERS
from app.main import app


@app.get(USERS)
async def get_users():
    return None  # TODO:
