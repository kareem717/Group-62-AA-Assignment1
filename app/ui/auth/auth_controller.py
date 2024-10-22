from entities.account import Account
from flask import render_template


class AuthController:
    def __init__(self, account_service):
        self.account_service = account_service

    def create_account(self, incoming_data):
        account = Account(
            incoming_data.get("user_name", None),
            incoming_data.get("first_name", None),
            incoming_data.get("last_name", None),
        )
        account_id = self.account_service.create(account)
        account.account_id = account_id
        return account.__dict__

    def get_create_account_form(self):
        return render_template("/auth/sign-up.html")
