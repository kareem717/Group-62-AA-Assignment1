from entities.account import Account

"""
This module provides the storage interface for Account entities.
"""
class AccountStorage:
    def add(self, account: Account) -> int:
        raise NotImplementedError()
