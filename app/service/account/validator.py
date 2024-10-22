from entities.account import Account
from storage.storage import AccountStorage
from ..exceptions import (
    InvalidEmailException,
    InvalidPasswordException,
    AccountAlreadyExistsException,
)


class AccountValidator:

    def __init__(self, storage: AccountStorage):
        self._storage = storage

    def validate(self, account: Account) -> Exception | None:
        if account.email is None or account.email == "":
            return InvalidEmailException()
        if account.password is None or account.password == "":
            return InvalidPasswordException()
        if self._storage.find_by_email(account.email):
            return AccountAlreadyExistsException()
        return None


#
