from entities.account import Account
from flask import render_template, redirect, session

class AuthController:
    def __init__(self, account_service):
        self.account_service = account_service

    def create_account(self, incoming_data):
        account = Account(
            email=incoming_data.get("email", None),
            password=incoming_data.get("password", None),
        )

        _, error_map = self.account_service.create(
            account, incoming_data.get("terms", False)
        )

        if error_map.has_errors():
            return {"success": False, "errors": error_map}
        else:
            return{"success": True, "user_id": account.id}

    def authenticate(self, incoming_data, session, jwt_secret):
        _, error_map = self.account_service.authenticate(
            email=incoming_data.get("email", None),
            password=incoming_data.get("password", None),
            jwt_secret=jwt_secret,
            session=session,
        )

        if error_map is not None and error_map.has_errors():
            return render_template("/auth/login.html", errors=error_map)
        else:
            return redirect("/")

    def logout(self):
        session.pop("account_id", None)
        return redirect("/")

    def get_create_account_form(self):
        return render_template("/auth/sign-up.html", errors=None)

    def get_login_form(self):
        return render_template("/auth/login.html", errors=None)
