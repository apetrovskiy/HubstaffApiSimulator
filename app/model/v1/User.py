from typing import List

from pydantic import BaseModel

from app.model.v1.Organization import Organization
from app.model.v1.Project import Project


class User(BaseModel):
    id: int
    name: str
    last_activity: str
    email: str
    organizations: List[Organization]
    projects: List[Project]
