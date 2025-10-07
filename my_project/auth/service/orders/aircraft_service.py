from typing import List

from my_project.auth.dao import aircraft_dao
from my_project.auth.service.general_service import GeneralService


class AircraftService(GeneralService):

    _dao = aircraft_dao

    def get_aircrafts_after_airline(self, airline_id: int) -> List[object]:
        return self._dao.get_aircrafts_after_airline(airline_id)
