from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:

    app.register_blueprint(err_handler_bp)

    from .orders.aircraft_route import aircraft_bp
    from .orders.airline_route import airline_bp
    from .orders.airport_route import airport_bp
    from .orders.crew_route import crew_bp
    from .orders.flight_route import flight_bp
    from .orders.flighthistory_route import flighthistory_bp
    from .orders.maintenance_route import maintenance_bp
    from .orders.pilot_route import pilot_bp
    from .orders.registration_route import registration_bp
    from .orders.route_route import route_bp
    from .orders.airline_airport_route import airline_airport_bp

    app.register_blueprint(aircraft_bp)
    app.register_blueprint(airline_bp)
    app.register_blueprint(airport_bp)
    app.register_blueprint(crew_bp)
    app.register_blueprint(flight_bp)
    app.register_blueprint(flighthistory_bp)
    app.register_blueprint(maintenance_bp)
    app.register_blueprint(pilot_bp)
    app.register_blueprint(registration_bp)
    app.register_blueprint(route_bp)
    app.register_blueprint(airline_airport_bp)
