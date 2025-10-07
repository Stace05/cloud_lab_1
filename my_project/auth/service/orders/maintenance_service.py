from typing import List

from my_project.auth.dao import maintenance_dao
from my_project.auth.service.general_service import GeneralService


class MaintenanceService(GeneralService):
    _dao = maintenance_dao

    def get_maintenances_after_aircraft(self, aircraft_id: int) -> List[object]:
        return self._dao.get_maintenances_after_aircraft(aircraft_id)
