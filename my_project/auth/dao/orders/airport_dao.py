from my_project.auth.dao.general_dao import GeneralDAO
from my_project.auth.domain import Airport


class AirportDAO(GeneralDAO):
    _domain_type = Airport
