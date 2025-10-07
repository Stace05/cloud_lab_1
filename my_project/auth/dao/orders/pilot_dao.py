from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Pilot


class PilotDAO(GeneralDAO):
    _domain_type = Pilot
