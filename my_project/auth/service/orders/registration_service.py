from typing import List

from my_project.auth.dao import registration_dao
from my_project.auth.service.general_service import GeneralService


class RegistrationService(GeneralService):
    _dao = registration_dao

    def get_registrations_after_aircraft(self, aircraft_id: int) -> List[object]:
        return self._dao.get_registrations_after_aircraft(aircraft_id)
