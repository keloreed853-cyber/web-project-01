import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_hello_world(client):
    """Test the hello-world endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_hello_name(client, monkeypatch):
    """Test the hello-world endpoint with a name."""
    monkeypatch.setenv('NAME', 'Gemini')
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, Gemini!" in response.data

def test_health_check(client):
    """Test the health check endpoint."""
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data
