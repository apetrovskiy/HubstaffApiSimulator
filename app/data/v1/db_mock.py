from datetime import datetime
from typing import List

from app.model.v1.users.Organization import Organization
from app.model.v1.users.Project import Project
from app.model.v1.users.User import User

hubstaff_users: List[User] = [User(
    id=11111,
    name="user1",
    last_activity=str(datetime.today()),
    email="email1@email.com",
    organizations=[Organization(
        id=111, name="org1", last_activity=str(datetime.today())
    )],
    projects=[Project(
        id=1111, name="proj1", last_activity=str(datetime.today()), status="ok"
    )]
), User(
    id=11112,
    name="user2",
    last_activity=str(datetime.today()),
    email="email2@email.com",
    organizations=[Organization(
        id=112, name="org2", last_activity=str(datetime.today())
    )],
    projects=[Project(
        id=1112, name="proj2", last_activity=str(datetime.today()), status="ok"
    )]
), User(
    id=11113,
    name="user3",
    last_activity=str(datetime.today()),
    email="email3@email.com",
    organizations=[Organization(
        id=113, name="org3", last_activity=str(datetime.today())
    )],
    projects=[Project(
        id=1113, name="proj3", last_activity=str(datetime.today()), status="ok"
    )]
)]
