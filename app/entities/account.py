from datetime import datetime


class Account:
    def __init__(
        self,
        id=None,
        email=None,
        password=None,
        created_at=datetime.now(),
        updated_at=None,
        deleted_at=None,
    ):
        self.id = id
        self.email = email
        self.password = password
        self.created_at = created_at
        self.updated_at = updated_at
        self.deleted_at = deleted_at
