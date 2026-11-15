from fastapi.testclient import TestClient

from add import add_numbers
from app import app, _observations


def test_add_numbers():
    assert add_numbers(2, 3) == 5


def test_add_endpoint():
    _observations.clear()
    response = TestClient(app).post("/add", json={"a": 2, "b": 3})
    assert response.status_code == 200
    assert response.json() == {"a": 2, "b": 3, "result": 5}


def test_evidently_report_requires_observations():
    _observations.clear()
    response = TestClient(app).get("/evidently-report")
    assert response.status_code == 400
