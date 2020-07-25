from fastapi.testclient import TestClient

from app.common.status_codes import OK
from app.common.v1.urls import USERS
from app.data.v1.db_mock import hubstaff_users
from app.main import app

client = TestClient(app)


def test_get_users():
    response = client.get(USERS)
    assert OK == response.status_code
    assert hubstaff_users == response.json()
