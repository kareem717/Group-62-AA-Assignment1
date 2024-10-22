import hashlib
from entities.account import Account
from .validator import AccountValidator
from storage.sqlite_storage import SqliteAccountStorage
from ..error_map import ErrorMap

"""
This module provides the service interface for Account entities.
"""


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


class AccountService:
    def __init__(self):
        self._account_storage = SqliteAccountStorage()
        self._account_validator = AccountValidator(self._account_storage)

    def create(self, account: Account, terms: bool) -> tuple[int, ErrorMap]:
        # Check if terms and conditions are accepted
        if not terms:
            return 0, ErrorMap().add_error(
                "terms", "You must agree to the terms and conditions"
            )

        # Check if account already exists
        existing_account = self._account_storage.get_by_email(account.email)
        if existing_account:
            if existing_account.password == hash_password(account.password):
                return 0, ErrorMap().add_error(
                    "email", "Account already exists, please sign in"
                )

        error_map = self._account_validator.validate(account)
        if error_map.has_errors():
            return 0, error_map

        # Hash password
        account.password = hash_password(account.password)

        return self._account_storage.create(account), error_map

    def authenticate(self, email: str, password: str) -> tuple[Account, ErrorMap]:
        account = self._account_storage.get_by_email(email)
        if account is None or account.password != hash_password(password):
            return Account(), ErrorMap().add_error("email", "Invalid email or password")

        return account, ErrorMap()
