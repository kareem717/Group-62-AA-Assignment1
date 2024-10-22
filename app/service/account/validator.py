from entities.account import Account
from storage.storage import AccountStorage


class AccountValidator:

    def __init__(self, storage: AccountStorage):
        self._storage = storage

    def validate(self, account: Account) -> bool:
        if account.first_name is None or account.first_name == "":
            return False
        if account.last_name is None or account.last_name == "":
            return False
        if self._storage.find_by_user_name(account.user_name):
            return False
        return True
# 