from .orders.aircraft_service import AircraftService
from .orders.airline_service import AirlineService
from .orders.airport_service import AirportService
from .orders.crew_service import CrewService
from .orders.flight_service import FlightService
from .orders.flighthistory_service import FlightHistoryService
from .orders.maintenance_service import MaintenanceService
from .orders.pilot_service import PilotService
from .orders.registration_service import RegistrationService
from .orders.route_service import RouteService
from .orders.airlline_airport_service import AirlineAirportService

aircraft_service = AircraftService()
airline_service = AirlineService()
airport_service = AirportService()
crew_service = CrewService()
flight_service = FlightService()
flighthistory_service = FlightHistoryService()
maintenance_service = MaintenanceService()
pilot_service = PilotService()
registration_service = RegistrationService()
route_service = RouteService()
airlline_airport_service = AirlineAirportService()
