from my_project.auth.dao import pilot_dao
from my_project.auth.service.general_service import GeneralService


class PilotService(GeneralService):
    _dao = pilot_dao
