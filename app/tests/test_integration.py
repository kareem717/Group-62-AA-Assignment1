import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app_instance as app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_user_auth_integration(client):
    """Test the integration between AuthController and AccountService"""
    response = client.post('/sign-up', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 302

    redirected_response = client.get('/')
    assert redirected_response.status_code == 200
    assert b'Welcome' in redirected_response.data
    
    login_response = client.post('/login', data={
        'email': 'testuser@example.com',
        'password': 'testpassword'
    })
    print(login_response.data.decode('utf-8'))
    assert login_response.status_code == 200
    assert '<a href="/logout"' in login_response.data.decode('utf-8')

def test_flight_booking_integration(client):
    """Test the integration between FlightController and FlightService"""
    response = client.get('/flights')
    assert response.status_code == 200
    assert b'Flights' in response.data

def test_homepage_integration(client):
    response = client.get('/')
    print(response.data.decode('utf-8'))
    assert response.status_code == 200
    assert "Sign Up" in response.data.decode('utf-8')