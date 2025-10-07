from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import pilot_controller
from my_project.auth.domain import Pilot

pilot_bp = Blueprint('pilots', __name__, url_prefix='/pilots')


@pilot_bp.get('')
def get_all_pilots() -> Response:
    """
    Get all pilots
    ---
    tags:
      - Pilot
    responses:
      200:
        description: List of all pilots
    """
    return make_response(jsonify(pilot_controller.find_all()), HTTPStatus.OK)


@pilot_bp.post('')
def create_pilot() -> Response:
    """
    Create new pilot
    ---
    tags:
      - Pilot
    parameters:
      - in: body
        name: pilot
        description: Pilot data
        required: true
        schema:
          type: object
          properties:
            pilot_name:
              type: string
              description: Pilot first name
            pilot_surname:
              type: string
              description: Pilot last name
            license_number:
              type: string
              description: License number
            total_flight_hours:
              type: integer
              description: Total flight hours
    responses:
      201:
        description: Pilot created successfully
    """
    content = request.get_json()
    pilot = Pilot.create_from_dto(content)
    pilot_controller.create(pilot)
    return make_response(jsonify(pilot.put_into_dto()), HTTPStatus.CREATED)


@pilot_bp.get('/<int:pilot_id>')
def get_pilot(pilot_id: int) -> Response:
    """
    Get pilot by ID
    ---
    tags:
      - Pilot
    parameters:
      - in: path
        name: pilot_id
        type: integer
        required: true
        description: Pilot ID
    responses:
      200:
        description: Pilot data
      404:
        description: Pilot not found
    """
    return make_response(jsonify(pilot_controller.find_by_id(pilot_id)), HTTPStatus.OK)


@pilot_bp.put('/<int:pilot_id>')
def update_pilot(pilot_id: int) -> Response:
    """
    Update pilot by ID
    ---
    tags:
      - Pilot
    parameters:
      - in: path
        name: pilot_id
        type: integer
        required: true
        description: Pilot ID
      - in: body
        name: pilot
        description: Updated pilot data
        required: true
        schema:
          type: object
          properties:
            pilot_name:
              type: string
              description: Pilot first name
            pilot_surname:
              type: string
              description: Pilot last name
            license_number:
              type: string
              description: License number
            total_flight_hours:
              type: integer
              description: Total flight hours
    responses:
      200:
        description: Pilot updated successfully
      404:
        description: Pilot not found
    """
    content = request.get_json()
    pilot = Pilot.create_from_dto(content)
    pilot_controller.update(pilot_id, pilot)
    return make_response("Pilot updated", HTTPStatus.OK)


@pilot_bp.patch('/<int:pilot_id>')
def patch_pilot(pilot_id: int) -> Response:
    """
    Partially update pilot by ID
    ---
    tags:
      - Pilot
    parameters:
      - in: path
        name: pilot_id
        type: integer
        required: true
        description: Pilot ID
      - in: body
        name: pilot
        description: Partial pilot data
        required: true
        schema:
          type: object
          properties:
            pilot_name:
              type: string
              description: Pilot first name
            pilot_surname:
              type: string
              description: Pilot last name
            license_number:
              type: string
              description: License number
            total_flight_hours:
              type: integer
              description: Total flight hours
    responses:
      200:
        description: Pilot updated successfully
      404:
        description: Pilot not found
    """
    content = request.get_json()
    pilot_controller.patch(pilot_id, content)
    return make_response("Pilot updated", HTTPStatus.OK)


@pilot_bp.delete('/<int:pilot_id>')
def delete_pilot(pilot_id: int) -> Response:
    """
    Delete pilot by ID
    ---
    tags:
      - Pilot
    parameters:
      - in: path
        name: pilot_id
        type: integer
        required: true
        description: Pilot ID
    responses:
      200:
        description: Pilot deleted successfully
      404:
        description: Pilot not found
    """
    pilot_controller.delete(pilot_id)
    return make_response("Pilot deleted", HTTPStatus.OK)


