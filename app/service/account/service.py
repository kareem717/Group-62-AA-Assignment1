from ..exceptions import InvalidAccountException
from entities.account import Account
from .validator import AccountValidator
from storage.storage import AccountStorage

"""
This module provides the service interface for Account entities.
"""


class AccountService:
    def __init__(self):
        self._account_storage = AccountStorage()
        self._account_validator = AccountValidator(self._account_storage)

    def create(self, account: Account) -> int:
        if not self._account_validator.validate(account):
            raise InvalidAccountException()
        return self._account_storage.add(account)