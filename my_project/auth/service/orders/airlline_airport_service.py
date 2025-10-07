from typing import List

from my_project.auth.dao import airline_airport_dao
from my_project.auth.service.general_service import GeneralService


class AirlineAirportService(GeneralService):
    _dao = airline_airport_dao

    def get_airports_after_airline(self, airline_id: int) -> List[object]:
        return self._dao.get_airports_after_airline(airline_id)

    def get_airlines_after_airport(self, airport_id: int) -> List[object]:
        return self._dao.get_airlines_after_airport(airport_id)
