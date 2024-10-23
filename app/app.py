from flask import Flask, request, send_from_directory, session
from service.account.service import AccountService
from presentation.auth.auth_controller import AuthController
from presentation.home.home_controller import HomeController
import os
from service.flight.service import FlightService
from presentation.flights.flight_controller import FlightController

app = Flask(__name__, static_folder="static")

# Read session secret from .env file
app.secret_key = os.getenv("SESSION_SECRET")

account_service = AccountService()
auth_controller = AuthController(account_service)
home_controller = HomeController(account_service)

flight_service = FlightService()
flight_controller = FlightController(flight_service)

JWT_SECRET = os.getenv("JWT_SECRET")

@app.route("/", methods=["GET"])
def index():
    return home_controller.get_home_page(session, JWT_SECRET)


@app.route("/static/<path:filename>")
def static_files(filename):
    return send_from_directory(app.static_folder, filename)


@app.route("/sign-up", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        return auth_controller.create_account(request.form)
    if request.method == "GET":
        return auth_controller.get_create_account_form()


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        return auth_controller.authenticate(request.form, session, JWT_SECRET)
    if request.method == "GET":
        return auth_controller.get_login_form()

@app.route("/logout", methods=["GET"])
def logout():
    return auth_controller.logout()


@app.route("/flights", methods=["GET"])
def flights():
    return flight_controller.get_flights()


if __name__ == "__main__":
    app.run(debug=True, port=5007)
