from platform_api.app import create_app
from fastapi.testclient import TestClient

def test_health(app_client: TestClient):
    req = app_client.get("/health")
    assert req.status_code == 200
    assert req.text == '"Health Check"'