from my_project.auth.dao import airport_dao
from my_project.auth.service.general_service import GeneralService


class AirportService(GeneralService):
    _dao = airport_dao
