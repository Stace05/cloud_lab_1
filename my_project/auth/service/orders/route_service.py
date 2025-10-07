from my_project.auth.dao import route_dao
from my_project.auth.service.general_service import GeneralService


class RouteService(GeneralService):
    _dao = route_dao
