from fastapi.testclient import TestClient

from app.common.status_codes import OK
from app.common.v1.urls import USERS, USER
from app.data.v1.db_mock import hubstaff_users, USER01_ID
from app.main import app1

client = TestClient(app1)


def test_get_users():
    response = client.get(USERS)
    assert OK == response.status_code
    assert hubstaff_users == response.json()


def test_get_user_by_id():
    response = client.get(USER.format(id=USER01_ID))
    assert OK == response.status_code
    assert [x for x in hubstaff_users
            if x.id == USER01_ID][0] == response.json()
