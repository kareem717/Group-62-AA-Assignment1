import sqlite3
from entities.account import Account
from storage.storage import Storage, AccountStorage


class SqliteStorage(Storage):

    DB_FILE = ":memory:"
    CREATE_ACCOUNTS_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS accounts (
        id SERIAL PRIMARY KEY, 
        email TEXT NOT NULL, 
        password TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP,
        deleted_at TIMESTAMP
    )
    """

    def __init__(self):
        print("Initializing SqliteStorage")
        self._connection = sqlite3.connect(self.DB_FILE, check_same_thread=False)
        cursor = self._connection.cursor()
        print("Creating accounts table")
        cursor.execute(self.CREATE_ACCOUNTS_TABLE_STATEMENT)
        cursor.close()
        self._connection.commit()
        print("SqliteStorage initialized")


class SqliteAccountStorage(SqliteStorage):
    def create(self, account):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (email, password) VALUES (?, ?)",
            (account.email, account.password),
        )
        account_id = cursor.lastrowid
        cursor.close()
        self._connection.commit()
        account.id = account_id
        return account_id

    def get_by_email(self, email: str) -> Account | None:
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM accounts WHERE email = ?",
            (email,),
        )
        row = cursor.fetchone()
        cursor.close()
        self._connection.commit()
        if row is None:
            return None
        return self._row_to_account(row)

    def _row_to_account(self, row):
        account = Account(row[1], row[2])
        account.account_id = row[0]
        return account
