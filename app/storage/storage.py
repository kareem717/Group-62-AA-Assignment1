from entities.account import Account
from entities.flight import Flight

class Storage:
    pass


class AccountStorage(Storage):
    def create(self, account: Account) -> int:
        raise NotImplementedError()

    def get_by_email(self, email: str) -> Account:
        raise NotImplementedError()


class FlightStorage(Storage):
    def get_many(self) -> list[Flight]:
        raise NotImplementedError()
