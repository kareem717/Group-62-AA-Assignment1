import random

class Account:
    def __init__(self, email, password):
        # Generate random user id
        self.id = random.randint(1, 1000000)

        self.email = email
        self.password = password
