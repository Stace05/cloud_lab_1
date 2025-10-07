from my_project.auth.service import pilot_service
from my_project.auth.controller.general_controller import GeneralController


class PilotController(GeneralController):

    _service = pilot_service
