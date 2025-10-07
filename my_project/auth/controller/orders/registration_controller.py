from typing import List

from my_project.auth.service import registration_service
from my_project.auth.controller.general_controller import GeneralController


class RegistrationController(GeneralController):

    _service = registration_service

    def get_registrations_after_aircraft(self, aircraft_id) -> List[object]:
        return self._service.get_registrations_after_aircraft(aircraft_id)
