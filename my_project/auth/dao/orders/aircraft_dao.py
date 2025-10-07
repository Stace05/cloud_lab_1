from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Aircraft


class AircraftDAO(GeneralDAO):
    _domain_type = Aircraft

    def get_aircrafts_after_airline(self, airline_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_aircrafts_after_airline(:p1)"),
                                       {'p1': airline_id}).mappings().all()
        return [dict(row) for row in result]
