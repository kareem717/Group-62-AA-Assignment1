import re
from entities.account import Account
from storage.storage import AccountStorage
from ..error_map import ErrorMap


class AccountValidator:

    def __init__(self, storage: AccountStorage):
        self._storage = storage

    def validate(self, account: Account) -> ErrorMap:
        error_map = ErrorMap()

        if account.email is None or account.email == "":
            error_map.add_error("email", "Must not be empty")
        elif len(account.email) > 360:
            error_map.add_error("email", "Must be less than 360 characters")
        elif not re.match(
            r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", account.email
        ):
            error_map.add_error("email", "Invalid email")

        if account.password is None or account.password == "":
            error_map.add_error("password", "Must not be empty")
        elif len(account.password) < 8:
            error_map.add_error("password", "Must be at least 8 characters long")
        elif not re.match(r"^[a-zA-Z0-9]+$", account.password):
            error_map.add_error("password", "Must contain only letters and numbers")

        return error_map


#
