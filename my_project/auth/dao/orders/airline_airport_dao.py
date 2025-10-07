from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import AirlineAirport


class AirlineAirportDAO(GeneralDAO):
    _domain_type = AirlineAirport

    def get_airports_after_airline(self, airline_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_airports_after_airline(:p1)"),
                                       {"p1": airline_id}).mappings().all()
        return [dict(row) for row in result]

    def get_airlines_after_airport(self, airport_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_airlines_after_airport(:p1)"),
                                       {"p1": airport_id}).mappings().all()
        return [dict(row) for row in result]
