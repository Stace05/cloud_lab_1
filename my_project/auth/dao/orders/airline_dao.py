from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Airline


class AirlineDAO(GeneralDAO):
    _domain_type = Airline
