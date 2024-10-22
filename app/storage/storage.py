from entities.account import Account


class Storage:
    pass


class AccountStorage(Storage):
    def create(self, account: Account) -> int:
        raise NotImplementedError()

    def get_by_email(self, email: str) -> Account:
        raise NotImplementedError()
