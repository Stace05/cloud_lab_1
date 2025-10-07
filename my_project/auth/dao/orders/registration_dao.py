from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Registration


class RegistrationDAO(GeneralDAO):
    _domain_type = Registration

    def get_registrations_after_aircraft(self, aircraft_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_registrations_after_aircraft(:p1)"),
                                       {'p1': aircraft_id}).mappings().all()
        return [dict(row) for row in result]
