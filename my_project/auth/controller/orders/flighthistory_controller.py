from typing import List

from my_project.auth.service import flighthistory_service
from my_project.auth.controller.general_controller import GeneralController


class FlightHistoryController(GeneralController):

    _service = flighthistory_service

    def get_flighthistories_after_flight(self, flight_id) -> List[object]:
        return self._service.get_flighthistories_after_flight(flight_id)
