from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Route


class RouteDAO(GeneralDAO):
    _domain_type = Route
