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

        account_id, error_map = self.account_service.create(
            account, incoming_data.get("terms", False)
        )
        account.account_id = account_id



        if error_map.has_errors():
            return render_template("/auth/sign-up.html", errors=error_map)
        else:
            return render_template("/home/home.html", account=account)

    def authenticate(self, incoming_data):
        account, error_map = self.account_service.authenticate(
            incoming_data.get("email", None),
            incoming_data.get("password", None),
        )

        if error_map.has_errors():
            return render_template("/auth/sign-in.html", errors=error_map)
        else:
            return render_template("/home/home.html", account=account)

    def get_create_account_form(self):
        return render_template("/auth/sign-up.html", errors=None)
        
