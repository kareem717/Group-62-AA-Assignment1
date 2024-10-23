from flask import render_template


class FlightController:
    def __init__(self, flight_service):
        self.flight_service = flight_service

    def get_flights(self):
        flights = self.flight_service.get_many()
        return render_template("/flights/index.html", flights=flights, errors=None)
