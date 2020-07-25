from typing import List

from fastapi import APIRouter

from app.common.v1.urls import USERS
from app.data.v1.db_mock import hubstaff_users
from app.model.v1.users.User import User

router = APIRouter()


@router.get(USERS, response_model=List[User])
async def get_users():
    return hubstaff_users
