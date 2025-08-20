import json

from fastapi.testclient import TestClient

from requester_api.main import app as app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Execute query by adding /countries/?country=usa"
    }


def test_country_response():
    response = client.get("/countries/?country='USA'")
    assert response.status_code == 200
    json_output = json.loads(response.text)
    assert "state" in json_output
