from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import crew_controller
from my_project.auth.domain import Crew

crew_bp = Blueprint('crews', __name__, url_prefix='/crews')


@crew_bp.get('')
def get_all_crews() -> Response:
    """
    Get all crews
    ---
    tags:
      - Crew
    responses:
      200:
        description: List of all crews
    """
    return make_response(jsonify(crew_controller.find_all()), HTTPStatus.OK)


@crew_bp.post('')
def create_crew() -> Response:
    """
    Create new crew
    ---
    tags:
      - Crew
    parameters:
      - in: body
        name: crew
        description: Crew data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            pilot_id:
              type: integer
              description: Pilot ID
    responses:
      201:
        description: Crew created successfully
    """
    content = request.get_json()
    crew = Crew.create_from_dto(content)
    crew_controller.create(crew)
    return make_response(jsonify(crew.put_into_dto()), HTTPStatus.CREATED)


@crew_bp.get('/<int:crew_id>')
def get_crew(crew_id: int) -> Response:
    """
    Get crew by ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: crew_id
        type: integer
        required: true
        description: Crew ID
    responses:
      200:
        description: Crew data
      404:
        description: Crew not found
    """
    return make_response(jsonify(crew_controller.find_by_id(crew_id)), HTTPStatus.OK)


@crew_bp.put('/<int:crew_id>')
def update_crew(crew_id: int) -> Response:
    """
    Update crew by ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: crew_id
        type: integer
        required: true
        description: Crew ID
      - in: body
        name: crew
        description: Updated crew data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            pilot_id:
              type: integer
              description: Pilot ID
    responses:
      200:
        description: Crew updated successfully
      404:
        description: Crew not found
    """
    content = request.get_json()
    crew = Crew.create_from_dto(content)
    crew_controller.update(crew_id, crew)
    return make_response("Crew updated", HTTPStatus.OK)


@crew_bp.patch('/<int:crew_id>')
def patch_crew(crew_id: int) -> Response:
    """
    Partially update crew by ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: crew_id
        type: integer
        required: true
        description: Crew ID
      - in: body
        name: crew
        description: Partial crew data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            pilot_id:
              type: integer
              description: Pilot ID
    responses:
      200:
        description: Crew updated successfully
      404:
        description: Crew not found
    """
    content = request.get_json()
    crew_controller.patch(crew_id, content)
    return make_response("Crew updated", HTTPStatus.OK)


@crew_bp.delete('/<int:crew_id>')
def delete_crew(crew_id: int) -> Response:
    """
    Delete crew by ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: crew_id
        type: integer
        required: true
        description: Crew ID
    responses:
      200:
        description: Crew deleted successfully
      404:
        description: Crew not found
    """
    crew_controller.delete(crew_id)
    return make_response("Crew deleted", HTTPStatus.OK)


@crew_bp.get('/find-crew-by-flight/<int:flight_id>')
def get_crew_after_flight(flight_id: int) -> Response:
    """
    Find crew by flight ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
    responses:
      200:
        description: List of crew for the flight
      404:
        description: Flight not found
    """
    return make_response(jsonify(crew_controller.get_crew_after_flight(flight_id)),
                         HTTPStatus.OK)


@crew_bp.get('/find-crew-by-pilot/<int:pilot_id>')
def get_crew_after_pilot(pilot_id: int) -> Response:
    """
    Find crew by pilot ID
    ---
    tags:
      - Crew
    parameters:
      - in: path
        name: pilot_id
        type: integer
        required: true
        description: Pilot ID
    responses:
      200:
        description: List of crew for the pilot
      404:
        description: Pilot not found
    """
    return make_response(jsonify(crew_controller.get_crew_after_pilot(pilot_id)),
                         HTTPStatus.OK)