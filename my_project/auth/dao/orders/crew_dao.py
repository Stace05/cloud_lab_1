from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Crew


class CrewDAO(GeneralDAO):
    _domain_type = Crew

    def get_crew_after_flight(self, flight_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_crew_after_flight(:p1)"),
                                       {'p1': flight_id}).mappings().all()
        return [dict(row) for row in result]

    def get_crew_after_pilot(self, pilot_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_crew_after_pilot(:p1)"),
                                       {'p1': pilot_id}).mappings().all()
        return [dict(row) for row in result]

