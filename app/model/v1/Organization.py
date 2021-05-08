from pydantic import BaseModel


class Organization(BaseModel):
    id: int
    name: str
    last_activity: str
