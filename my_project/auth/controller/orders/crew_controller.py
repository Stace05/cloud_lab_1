from typing import List

from my_project.auth.service import crew_service
from my_project.auth.controller.general_controller import GeneralController


class CrewController(GeneralController):

    _service = crew_service

    def get_crew_after_flight(self, flight_id) -> List[object]:
        return self._service.get_crew_after_flight(flight_id)

    def get_crew_after_pilot(self, pilot_id) -> List[object]:
        return self._service.get_crew_after_pilot(pilot_id)
