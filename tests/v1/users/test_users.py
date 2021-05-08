from fastapi.testclient import TestClient

from app.common.status_codes import OK
from app.common.v1.urls import USERS, USER
from app.data.v1.db_mock import hubstaff_users, USER01_ID
from app.main import app1

client = TestClient(app1)


def test_get_users():
    response = client.get(USERS)
    assert response.status_code == OK
    assert response.json() == hubstaff_users


def test_get_user_by_id():
    response = client.get(USER.format(id=USER01_ID))
    assert response.status_code == OK
    assert response.json() == \
           [x for x in hubstaff_users if x.id == USER01_ID][0]
