from .orders.aircraft_dao import AircraftDAO
from .orders.airline_dao import AirlineDAO
from .orders.airport_dao import AirportDAO
from .orders.crew_dao import CrewDAO
from .orders.flight_dao import FlightDAO
from .orders.flighthistory_dao import FlightHistoryDAO
from .orders.maintenance_dao import MaintenanceDAO
from .orders.pilot_dao import PilotDAO
from .orders.registration_dao import RegistrationDAO
from .orders.route_dao import RouteDAO
from .orders.airline_airport_dao import AirlineAirportDAO

aircraft_dao = AircraftDAO()
airline_dao = AirlineDAO()
airport_dao = AirportDAO()
crew_dao = CrewDAO()
flight_dao = FlightDAO()
flighthistory_dao = FlightHistoryDAO()
maintenance_dao = MaintenanceDAO()
pilot_dao = PilotDAO()
registration_dao = RegistrationDAO()
route_dao = RouteDAO()
airline_airport_dao = AirlineAirportDAO()
