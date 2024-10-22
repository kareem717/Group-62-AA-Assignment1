import json
from entities.account import Account
from flask import render_template


class AuthController:
    def __init__(self, account_service):
        self.account_service = account_service

    def create_account(self, incoming_data):
        account = Account(
            incoming_data.get("email", None),
            incoming_data.get("password", None),
        )

        account_id = self.account_service.create(account)
        account.account_id = account_id
        return render_template("/home/home.html")

    def get_create_account_form(self):
        return render_template("/auth/sign-up.html")
