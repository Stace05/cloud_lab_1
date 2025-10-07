from my_project.auth.dao import airline_dao
from my_project.auth.service.general_service import GeneralService


class AirlineService(GeneralService):
    _dao = airline_dao
