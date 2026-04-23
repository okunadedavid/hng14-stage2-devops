import pytest
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from main import app

client = TestClient(app)

# Mock Redis inside app


@pytest.fixture(autouse=True)
def mock_redis(monkeypatch):
    fake_redis = MagicMock()
    fake_redis.lpush.return_value = 1
    fake_redis.hset.return_value = 1
    fake_redis.hget.return_value = b"completed"

    monkeypatch.setattr("main.r", fake_redis)
    return fake_redis


def test_create_job():
    res = client.post("/jobs")
    assert res.status_code == 200
    assert "job_id" in res.json()


def test_get_job_success():
    res = client.get("/jobs/test123")
    assert res.status_code == 200
    assert "status" in res.json()


def test_health_endpoint():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"
