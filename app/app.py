from flask import Flask, request, send_from_directory, session, redirect, render_template
from service.account.service import AccountService
from presentation.auth.auth_controller import AuthController
from presentation.home.home_controller import HomeController
import os
from service.flight.service import FlightService
from presentation.flights.flight_controller import FlightController
from dotenv import load_dotenv

load_dotenv()

app = Flask(
    __name__,
    static_folder="static",
    template_folder="templates"
)

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
        response = auth_controller.create_account(request.form)
        if response.get("success"):
            session["user_id"] = response["user_id"]
            return redirect('/')
        else:
            return render_template("auth/sign-up.html", errors=response.get("errors"))
    return render_template("auth/sign-up.html", errors=None)



@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        response = auth_controller.authenticate(request.form, session, JWT_SECRET)
        if response.get("success"):
            return redirect("/")
        else:
            return render_template("auth/login.html", error=response.get("errors"))
    return render_template("auth/login.html", errors=None)
    
@app.route("/logout", methods=["GET"])
def logout():
    session.clear()
    return redirect("/")


@app.route("/flights", methods=["GET"])
def flights():
    return flight_controller.get_flights()


if __name__ == "__main__":
    app.run(debug=True, port=5007)

app_instance = app