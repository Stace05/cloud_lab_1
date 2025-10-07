from typing import List

from my_project.auth.dao import flighthistory_dao
from my_project.auth.service.general_service import GeneralService


class FlightHistoryService(GeneralService):
    _dao = flighthistory_dao

    def get_flighthistories_after_flight(self, flight_id: int) -> List[object]:
        return self._dao.get_flighthistories_after_flight(flight_id)
