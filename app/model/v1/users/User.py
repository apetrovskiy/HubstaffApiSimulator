from typing import List

from pydantic import BaseModel

from app.model.v1.users.Organization import Organization
from app.model.v1.users.Project import Project


class User(BaseModel):
    id: int
    name: str
    last_activity: str
    email: str
    organizations: List[Organization]
    projects: List[Project]
