from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import FlightHistory


class FlightHistoryDAO(GeneralDAO):
    _domain_type = FlightHistory

    def get_flighthistories_after_flight(self, flight_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_flighthistories_after_flight(:p1)"),
                                       {'p1': flight_id}).mappings().all()
        return [dict(row) for row in result]
