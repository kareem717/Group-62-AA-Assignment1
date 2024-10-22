import random
from datetime import datetime


class Account:
    def __init__(self, email, password):
        # Generate random user id
        self.id = random.randint(1, 1000000)

        self.email = email
        self.password = password
        self.created_at = datetime.now()
        self.updated_at = None
        self.deleted_at = None
