from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import aircraft_controller
from my_project.auth.domain import Aircraft

aircraft_bp = Blueprint('aircrafts', __name__, url_prefix='/aircrafts')





@aircraft_bp.post('')
def create_aircraft() -> Response:
    """
    Create new aircraft
    ---
    tags:
      - Aircraft
    parameters:
      - in: body
        name: aircraft
        description: Aircraft data
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              description: Aircraft model
            registration_number:
              type: string
              description: Registration number
            airline_id:
              type: integer
              description: Airline ID
            total_flight_hours:
              type: integer
              description: total flight hours
    responses:
      201:
        description: Aircraft created successfully
    """
    content = request.get_json()
    aircraft = Aircraft.create_from_dto(content)
    aircraft_controller.create(aircraft)
    return make_response(jsonify(aircraft.put_into_dto()), HTTPStatus.CREATED)


@aircraft_bp.get('/<int:aircraft_id>')
def get_aircraft(aircraft_id: int) -> Response:
    """
    Get aircraft by ID
    ---
    tags:
      - Aircraft
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
    responses:
      200:
        description: Aircraft data
      404:
        description: Aircraft not found
    """
    return make_response(jsonify(aircraft_controller.find_by_id(aircraft_id)), HTTPStatus.OK)


@aircraft_bp.put('/<int:aircraft_id>')
def update_aircraft(aircraft_id: int) -> Response:
    """
    Update aircraft by ID
    ---
    tags:
      - Aircraft
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
      - in: body
        name: aircraft
        description: Updated aircraft data
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              description: Aircraft model
            registration_number:
              type: string
              description: Registration number
            airline_id:
              type: integer
              description: Airline ID
    responses:
      200:
        description: Aircraft updated successfully
      404:
        description: Aircraft not found
    """
    content = request.get_json()
    aircraft = Aircraft.create_from_dto(content)
    aircraft_controller.update(aircraft_id, aircraft)
    return make_response("Aircraft updated", HTTPStatus.OK)


@aircraft_bp.patch('/<int:aircraft_id>')
def patch_aircraft(aircraft_id: int) -> Response:
    """
    Partially update aircraft by ID
    ---
    tags:
      - Aircraft
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
      - in: body
        name: aircraft
        description: Partial aircraft data
        required: true
        schema:
          type: object
          properties:
            model:
              type: string
              description: Aircraft model
            registration_number:
              type: string
              description: Registration number
            airline_id:
              type: integer
              description: Airline ID
    responses:
      200:
        description: Aircraft updated successfully
      404:
        description: Aircraft not found
    """
    content = request.get_json()
    aircraft_controller.patch(aircraft_id, content)
    return make_response("Aircraft updated", HTTPStatus.OK)


@aircraft_bp.delete('/<int:aircraft_id>')
def delete_aircraft(aircraft_id: int) -> Response:
    """
    Delete aircraft by ID
    ---
    tags:
      - Aircraft
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
    responses:
      200:
        description: Aircraft deleted successfully
      404:
        description: Aircraft not found
    """
    aircraft_controller.delete(aircraft_id)
    return make_response("Aircraft deleted", HTTPStatus.OK)


@aircraft_bp.get('/find-aircrafts-by-airline/<int:airline_id>')
def get_aircrafts_after_airline(airline_id: int) -> Response:
    """
    Find aircrafts by airline ID
    ---
    tags:
      - Aircraft
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
    responses:
      200:
        description: List of aircrafts for the airline
      404:
        description: Airline not found
    """
    return make_response(jsonify(aircraft_controller.get_aircrafts_after_airline(airline_id)),
                         HTTPStatus.OK)