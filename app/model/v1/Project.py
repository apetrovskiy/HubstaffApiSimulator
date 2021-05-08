from pydantic import BaseModel


class Project(BaseModel):
    id: int
    name: str
    last_activity: str
    status: str
