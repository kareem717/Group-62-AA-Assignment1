import sqlite3
from entities.account import Account
from storage.storage import Storage
from entities.flight import Flight

class SqliteStorage(Storage):

    DB_FILE = ":memory:"

    CREATE_ACCOUNTS_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        email TEXT NOT NULL, 
        password TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP,
        deleted_at TIMESTAMP
    );
    """

    CREATE_FLIGHTS_TABLE_STATEMENT = """
    CREATE TABLE IF NOT EXISTS flights (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        origin TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure_date TIMESTAMP NOT NULL,
        return_date TIMESTAMP NOT NULL,
        seats_available INTEGER NOT NULL,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP,
        deleted_at TIMESTAMP
    );
    """
    
    SEED_FLIGHTS_STATEMENT = """
    INSERT INTO flights (origin, destination, departure_date, return_date, seats_available) VALUES ('SFO', 'LAX', '2024-01-01 10:00:00', '2024-01-02 12:00:00', 100);
    """

    def __init__(self):
        print("Initializing SqliteStorage")
        self._connection = sqlite3.connect(self.DB_FILE, check_same_thread=False)
        cursor = self._connection.cursor()
        print("Creating accounts table")
        cursor.execute(self.CREATE_ACCOUNTS_TABLE_STATEMENT)
        print("Creating flights table")
        cursor.execute(self.CREATE_FLIGHTS_TABLE_STATEMENT)
        print("Seeding flights")
        cursor.execute(self.SEED_FLIGHTS_STATEMENT)
        cursor.close()
        self._connection.commit()
        print("SqliteStorage initialized")

class SqliteAccountStorage(SqliteStorage):
    def create(self, account):
        cursor = self._connection.cursor()
        cursor.execute(
            "INSERT INTO accounts (email, password, created_at) VALUES (?, ?, ?)",
            (account.email, account.password, account.created_at),
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

    def get_by_id(self, account_id: int) -> Account | None:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM accounts WHERE id = ?", (account_id,))
        row = cursor.fetchone()
        cursor.close()
        self._connection.commit()
        if row is None:
            return None
        return self._row_to_account(row)

    def _row_to_account(self, row):
        account = Account(
            id=row[0],
            email=row[1],
            password=row[2],
            created_at=row[3],
            updated_at=row[4],
            deleted_at=row[5],
        )
        return account

class SqliteFlightStorage(SqliteStorage):
    def create(self, flight):
        cursor = self._connection.cursor()
        cursor.execute(
            """
            INSERT INTO flights (
                origin, 
                destination, 
                departure_date, 
                return_date, 
                seats_available, 
                created_at
            ) 
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                flight.origin,
                flight.destination,
                flight.departure_date,
                flight.return_date,
                flight.seats_available,
                flight.created_at,
            ),
        )
        flight_id = cursor.lastrowid
        cursor.close()
        self._connection.commit()
        flight.id = flight_id
        return flight_id

    def get_many(self) -> list[Flight]:
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM flights")
        rows = cursor.fetchall()
        cursor.close()
        self._connection.commit()

        if rows is None:
            return []

        return [self._row_to_flight(row) for row in rows]

    def _row_to_flight(self, row):
        flight = Flight(
            id=row[0],
            origin=row[1],
            destination=row[2],
            departure_date=row[3],
            return_date=row[4],
            seats_available=row[5],
            created_at=row[6],
            updated_at=row[7],
            deleted_at=row[8],
        )
        return flight
