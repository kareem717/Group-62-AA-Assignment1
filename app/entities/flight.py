from datetime import datetime

class Flight:
    def __init__(
        self,
        id=None,
        origin=None,
        destination=None,
        departure_date=None,
        return_date=None,
        seats_available=None,
        created_at=datetime.now(),
        updated_at=None,
        deleted_at=None,
    ):
        self.id = id
        self.origin = origin
        self.destination = destination
        self.departure_date = datetime.strptime(departure_date, '%Y-%m-%d %H:%M:%S')
        self.return_date = datetime.strptime(return_date, '%Y-%m-%d %H:%M:%S')
        self.seats_available = seats_available
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
