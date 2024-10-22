from entities.account import Account


class Storage:
    pass


class AccountStorage(Storage):
    def create(self, account: Account) -> int:
        raise NotImplementedError()
