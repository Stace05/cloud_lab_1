from typing import List

from my_project.auth.dao import flight_dao
from my_project.auth.service.general_service import GeneralService


class FlightService(GeneralService):
    _dao = flight_dao

    def get_flights_after_aircraft(self, aircraft_id: int) -> List[object]:
        return self._dao.get_flights_after_aircraft(aircraft_id)

