from my_project.auth.service import airline_service
from my_project.auth.controller.general_controller import GeneralController


class AirlineController(GeneralController):

    _service = airline_service
