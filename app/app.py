from flask import Flask, render_template, request, send_from_directory
from service.account.service import AccountService
from ui.auth.auth_controller import AuthController
from ui.home.home_controller import HomeController

app = Flask(__name__, static_folder="static")


account_service = AccountService()
auth_controller = AuthController(account_service)
home_controller = HomeController(account_service)


@app.route("/", methods=["GET"])
def index():
    return home_controller.get_home_page()


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return auth_controller.create_account(request.form)
    if request.method == "GET":
        return auth_controller.get_create_account_form()


@app.route("/login", methods=["GET"])
def login():
    return render_template("/auth/login.html")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
