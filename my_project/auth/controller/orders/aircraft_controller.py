from typing import List

from my_project.auth.service import aircraft_service
from my_project.auth.controller.general_controller import GeneralController


class AircraftController(GeneralController):

    _service = aircraft_service

    def get_aircrafts_after_airline(self, airline_id) -> List[object]:
        return self._service.get_aircrafts_after_airline(airline_id)
