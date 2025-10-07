from my_project.auth.service import route_service
from my_project.auth.controller.general_controller import GeneralController


class RouteController(GeneralController):

    _service = route_service
