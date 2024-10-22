from entities.account import Account
from flask import render_template


class HomeController:
    def __init__(self, account_service):
        self.account_service = account_service

    def get_home_page(self):
        return render_template("home/home.html")
