from typing import List

from my_project.auth.service import airlline_airport_service
from my_project.auth.controller.general_controller import GeneralController


class AirlineAirportController(GeneralController):

    _service = airlline_airport_service

    def get_airlines_after_airport(self, airport_id) -> List[object]:
        return self._service.get_airlines_after_airport(airport_id)

    def get_airports_after_airline(self, airline_id) -> List[object]:
        return self._service.get_airports_after_airline(airline_id)
