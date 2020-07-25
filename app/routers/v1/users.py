from typing import List

from app.common.v1.urls import USERS
from app.data.v1.db_mock import users
from app.main import app
from app.model.v1.users.User import User


@app.get(USERS, response_model=List[User])
async def get_users():
    return users
