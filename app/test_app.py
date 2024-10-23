import pytest
from app import app, mock_db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

# Test cases for sign-up functionality
def test_signup_invalid_email(client):
    response = client.post('/sign-up', data={
        'email': 'invalidemail',
        'password': 'password123',
        'terms': 'on'
    })
    assert response.status_code == 400
    assert b"Invalid email" in response.data

def test_signup_password_too_short(client):
    response = client.post('/sign-up', data={
        'email': 'valid@example.com',
        'password': 'short',
        'terms': 'on'
    })
    assert response.status_code == 400
    assert b"Password too short" in response.data

def test_signup_password_too_long(client):
    long_password = 'a' * 321
    response = client.post('/sign-up', data={
        'email': 'valid@example.com',
        'password': long_password,
        'terms': 'on'
    })
    assert response.status_code == 400
    assert b"Password too long" in response.data

def test_signup_success(client):
    response = client.post('/sign-up', data={
        'email': 'newuser@example.com',
        'password': 'password123',
        'terms': 'on'
    })
    assert response.status_code == 302
    assert response.headers['Location'] == '/login'
    assert len(mock_db['users']) == 1  # verify the user is added

def test_signup_existing_user(client):
    mock_db['users'].append({
        'email': 'existinguser@example.com',
        'password': 'password123'
    })
    response = client.post('/sign-up', data={
        'email': 'existinguser@example.com',
        'password': 'password123',
        'terms': 'on'
    })
    assert response.status_code == 400
    assert b"User already exists." in response.data

# Test cases for missing terms
def test_signup_missing_terms(client):
    response = client.post('/sign-up', data={
        'email': 'newuser@example.com',
        'password': 'password123',
        'terms': ''  # Simulate no checkbox
    })
    assert response.status_code == 400
    assert b"Please accept the terms and conditions." in response.data

# test case to ensure valid registration redirects correctly
def test_redirect_on_valid_registration(client):
    response = client.post('/sign-up', data={
        'email': 'validuser@example.com',
        'password': 'validpassword123',
        'terms': 'on'
    })
    assert response.status_code == 302  # redirect
    assert response.headers['Location'] == '/login'  # redirect to login page


# test cases for login functionality
def test_login_success(client):
    """Test successful login"""
    mock_db['users'].append({
        'email': 'loginuser@example.com',
        'password': 'password123'
    })
    response = client.post('/login', data={
        'email': 'loginuser@example.com',
        'password': 'password123'
    }, follow_redirects=True)  # follow the redirect to the index page
    
    assert response.status_code == 200
    assert b'SkySeat' in response.data  # verify 'SkySeat' appears in the rendered index page

def test_login_invalid_password(client):
    """Test login with incorrect password"""
    mock_db['users'].append({
        'email': 'loginuser@example.com',
        'password': 'password123'
    })
    response = client.post('/login', data={
        'email': 'loginuser@example.com',
        'password': 'wrongpassword'
    })
    assert response.status_code == 401
    assert b"Invalid email or password." in response.data

def test_login_user_not_found(client):
    """Test login with non-existent user"""
    response = client.post('/login', data={
        'email': 'nonexistentuser@example.com',
        'password': 'password123'
    })
    assert response.status_code == 401
    assert b"Invalid email or password." in response.data

def test_login_missing_fields(client):
    """Test login with missing fields"""
    response = client.post('/login', data={})
    assert response.status_code == 400
    assert b"Email and password are required." in response.data