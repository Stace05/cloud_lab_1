from typing import List

from my_project.auth.service import flight_service
from my_project.auth.controller.general_controller import GeneralController


class FlightController(GeneralController):

    _service = flight_service

    def get_flights_after_aircraft(self, aircraft_id) -> List[object]:
        return self._service.get_flights_after_aircraft(aircraft_id)
