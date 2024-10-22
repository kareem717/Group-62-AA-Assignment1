import uuid


class Account:
    def __init__(self, first_name, last_name):
        # Generate random user id
        self.user_id = uuid.uuid4()

        self.first_name = first_name
        self.last_name = last_name
