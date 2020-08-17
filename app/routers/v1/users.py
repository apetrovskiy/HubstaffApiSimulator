from typing import List

from fastapi import APIRouter

from app.common.v1.urls import USERS, USER
from app.data.v1.db_mock import hubstaff_users
from app.model.v1.User import User

router: APIRouter = APIRouter()


@router.get(USERS, response_model=List[User])
async def get_users():
    return hubstaff_users


@router.get(USER, response_model=User)
async def get_user_by_id(user_id: int):
    result: User = [x for x in hubstaff_users if x.id == user_id][0]
    return result
