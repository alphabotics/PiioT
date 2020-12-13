from fastapi.testclient import TestClient
from App.main import app

client = TestClient(app)

def objectKeyExist(key, dict_json):
    if key in dict_json:
        return True
    return False

def test_get_users():
    response = client.get("/api/admin/users/")
    data_json = response.json()
    first_user = data_json['data'][0]
    assert response.status_code == 200
    assert objectKeyExist('first_name', first_user)
    # assert first_user['first_name'] == 'aa'
    assert first_user['first_name'] == 'User1'
    assert first_user['last_name'] == 'User'