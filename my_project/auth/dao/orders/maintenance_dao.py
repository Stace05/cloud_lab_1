from typing import List, Dict, Any

import sqlalchemy

from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Maintenance


class MaintenanceDAO(GeneralDAO):
    _domain_type = Maintenance

    def get_maintenances_after_aircraft(self, aircraft_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_maintenances_after_aircraft(:p1)"),
                                       {'p1': aircraft_id}).mappings().all()
        return [dict(row) for row in result]
