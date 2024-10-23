from entities.flight import Flight
from storage.sqlite_storage import SqliteFlightStorage

"""
This module provides the service interface for Flight entities.
"""


class FlightService:
    def __init__(self):
        self._flight_storage = SqliteFlightStorage()

    def get_many(self) -> list[Flight]:
        return self._flight_storage.get_many()
