from typing import List

from my_project.auth.service import maintenance_service
from my_project.auth.controller.general_controller import GeneralController


class MaintenanceController(GeneralController):

    _service = maintenance_service

    def get_maintenances_after_aircraft(self, aircraft_id) -> List[object]:
        return self._service.get_maintenances_after_aircraft(aircraft_id)
