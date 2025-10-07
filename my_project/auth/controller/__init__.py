from .orders.aircraft_controller import AircraftController
from .orders.airline_controller import AirlineController
from .orders.airport_controller import AirportController
from .orders.crew_controller import CrewController
from .orders.flight_controller import FlightController
from .orders.flighthistory_controller import FlightHistoryController
from .orders.maintenance_controller import MaintenanceController
from .orders.pilot_controller import PilotController
from .orders.registration_controller import RegistrationController
from .orders.route_controller import RouteController
from .orders.airline_airport_controller import AirlineAirportController

aircraft_controller = AircraftController()
airline_controller = AirlineController()
airport_controller = AirportController()
crew_controller = CrewController()
flight_controller = FlightController()
flighthistory_controller = FlightHistoryController()
maintenance_controller = MaintenanceController()
pilot_controller = PilotController()
registration_controller = RegistrationController()
route_controller = RouteController()
airline_airport_controller = AirlineAirportController()
