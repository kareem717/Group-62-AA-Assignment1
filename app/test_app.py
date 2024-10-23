import pytest
from service.account.service import AccountService
from entities.account import Account
from service.error_map import ErrorMap


@pytest.fixture
def account_service():
    return AccountService()


def test_create_account_success(account_service):
    account = Account(email="newuser@example.com", password="password123")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id != 0
    assert not error_map.has_errors()


def test_create_account_missing_terms(account_service):
    account = Account(email="newuser@example.com", password="password123")
    terms = False
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert (
        error_map.get_errors()["terms"] == "You must agree to the terms and conditions"
    )


def test_create_account_existing_email(account_service):
    account = Account(email="existinguser@example.com", password="password123")
    terms = True
    # Simulate existing account
    account_service._account_storage.create(account)

    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["email"] == "Account already exists, please sign in"


def test_create_account_invalid_email(account_service):
    account = Account(email="invalidemail", password="password123")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["email"] == "Invalid email"


def test_create_account_invalid_password(account_service):
    account = Account(email="invalidemail@example.com", password="short")
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["password"] == "Must be at least 8 characters long"


def test_create_account_invalid_password_length(account_service):
    account = Account(email="invalidemail@example.com", password=("A" * 32))
    terms = True
    account_id, error_map = account_service.create(account, terms)

    assert account_id == 0
    assert error_map.has_errors()
    assert error_map.get_errors()["password"] == "Must be less than 321 characters"
