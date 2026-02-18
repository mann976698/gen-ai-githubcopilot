import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Use a unique email for testing
    test_email = "pytest_user@example.com"
    activity = list(client.get("/activities").json().keys())[0]
    # Sign up
    signup = client.post(f"/activities/{activity}/signup?email={test_email}")
    assert signup.status_code in (200, 400)  # 400 if already signed up
    # Unregister
    unregister = client.delete(f"/activities/{activity}/participants/{test_email}")
    assert unregister.status_code in (200, 404)  # 404 if not found
