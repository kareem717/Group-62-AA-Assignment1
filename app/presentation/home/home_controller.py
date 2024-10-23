from flask import render_template

class HomeController:
    def __init__(self, account_service):
        self.account_service = account_service

    def get_home_page(self, session, jwt_secret):
        account = self.account_service.get_account_from_session(session, jwt_secret)
        return render_template("home/home.html", account=account)
