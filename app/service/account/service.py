from entities.account import Account
from .validator import AccountValidator
from storage.sqlite_storage import SqliteAccountStorage

"""
This module provides the service interface for Account entities.
"""


class AccountService:
    def __init__(self):
        self._account_storage = SqliteAccountStorage()
        self._account_validator = AccountValidator(self._account_storage)

    def create(self, account: Account) -> int:
        error = self._account_validator.validate(account)
        if error:
            raise error

        return self._account_storage.create(account)
