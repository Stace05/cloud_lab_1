from typing import List

from my_project.auth.dao import crew_dao
from my_project.auth.service.general_service import GeneralService


class CrewService(GeneralService):
    _dao = crew_dao

    def get_crew_after_flight(self, flight_id: int) -> List[object]:
        return self._dao.get_crew_after_flight(flight_id)

    def get_crew_after_pilot(self, pilot_id: int) -> List[object]:
        return self._dao.get_crew_after_pilot(pilot_id)
