import pytest
import sqlite3
from service.account.service import AccountService
from storage.sqlite_storage import SqliteAccountStorage, SqliteFlightStorage
from presentation.auth.auth_controller import AuthController
from entities.account import Account
from entities.flight import Flight
from app.app import app

@pytest.fixture
def account_service():
    return AccountService()

@pytest.fixture
def auth_controller(account_service):
    with app.app_context():
        yield AuthController(account_service)

@pytest.fixture
def account_service():
    return AccountService()

@pytest.fixture
def db_connection():
    connection = sqlite3.connect(":memory:")
    yield connection
    connection.close()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@pytest.fixture
def account_storage(db_connection):
    return SqliteAccountStorage()

@pytest.fixture
def flight_storage(db_connection):
    return SqliteFlightStorage()



def test_create_account_success(account_service):
    account = Account(email="newuser@example.com", password="password123")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id != 0
    assert not error_map.has_errors()


def test_create_accout_missing_terms(account_service):
    account = Account(email="newuser@example.com", password="password123")
    terms = False

    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert (
        error_map.get_errors()["terms"] == "You must agree to the terms and conditions"
    )


def test_create_account_existing_eail(account_service):
    account = Account(email="existinguser@example.com", password="password123")
    terms = True
    # Simulate existing account
    account_service._account_storage.create(account)

    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["email"] == "Account already exists, please sign in"


def test_create_account_invalid_emal(account_service):
    account = Account(email="invalidemail", password="password123")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["email"] == "Invalid email"


def test_create_account_invalid_password_short(account_service):
    account = Account(email="invalidemail@example.com", password="short")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0

    assert error_map.has_errors()
    assert error_map.get_errors()["password"] == "Must be at least 8 characters long"


def test_create_account_invalid_passwordlength(account_service):

    account = Account(email="invalidemail@example.com", password=("A" * 321))
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0

    assert error_map.has_errors()

    assert error_map.get_errors()["password"] == "Must be less than 321 characters"


# test cases for login functionality
def test_login_success(client, account_service):
    account = Account(email="invalidemail@example.com", password="password123")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id != 0
    assert not error_map.has_errors()

    response = client.post(
        "/login",
        data={"email": "invalidemail@example.com", "password": "password123"},
    )

    assert response.status_code == 200

def test_flight_entity():
    from entities.flight import Flight
    from datetime import datetime

    flight = Flight(
        id=1,
        origin="New York",
        destination="Los Angeles",
        departure_date="2023-10-01 10:00:00",
        return_date="2023-10-01 13:00:00",
        seats_available=100
    )

    assert flight.id == 1
    assert flight.origin == "New York"
    assert flight.destination == "Los Angeles"
    assert flight.departure_date == datetime.strptime("2023-10-01 10:00:00", '%Y-%m-%d %H:%M:%S')
    assert flight.return_date == datetime.strptime("2023-10-01 13:00:00", '%Y-%m-%d %H:%M:%S')
    assert flight.seats_available == 100
    assert isinstance(flight.created_at, datetime)
    assert flight.updated_at is None
    assert flight.deleted_at is None

def test_create_account_with_missing_email(client):
    response = client.post("/sign-up", data={
        "email": None, 
        "password": "password123",
        "terms": True
    })

    assert b"email" in response.data 
    assert response.status_code == 200 

def test_get_account_by_email(account_storage):
    account = Account(email="test@example.com", password="securepassword", created_at="2024-01-01")
    account_storage.create(account)
    retrieved_account = account_storage.get_by_email("test@example.com")
    assert retrieved_account is not None
    assert retrieved_account.email == "test@example.com"

def test_get_account_by_id(account_storage):
    account = Account(email="test2@example.com", password="securepassword", created_at="2024-01-01")
    account_id = account_storage.create(account)
    retrieved_account = account_storage.get_by_id(account_id)
    assert retrieved_account is not None
    assert retrieved_account.id == account_id

def test_get_many_flights(flight_storage):
    flight = Flight(
        origin="SFO", 
        destination="LAX", 
        departure_date="2024-01-01 10:00:00",
        return_date="2024-01-02 12:00:00", 
        seats_available=50, 
        created_at="2024-01-01"
    )
    flight_storage.create(flight)
    flights = flight_storage.get_many()
    assert len(flights) > 0
    assert flights[0].origin == "SFO"