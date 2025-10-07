from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import flighthistory_controller
from my_project.auth.domain import FlightHistory

flighthistory_bp = Blueprint('flighthistories', __name__, url_prefix='/flighthistories')


@flighthistory_bp.get('')
def get_all_flighthistories() -> Response:
    """
    Get all flight histories
    ---
    tags:
      - Flight History
    responses:
      200:
        description: List of all flight histories
    """
    return make_response(jsonify(flighthistory_controller.find_all()), HTTPStatus.OK)


@flighthistory_bp.post('')
def create_flighthistory() -> Response:
    """
    Create new flight history
    ---
    tags:
      - Flight History
    parameters:
      - in: body
        name: flighthistory
        description: Flight history data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            actual_departure_time:
              type: string
              format: date-time
              description: Actual departure time
            actual_arrival_time:
              type: string
              format: date-time
              description: Actual arrival time
            status:
              type: string
              description: Flight status
    responses:
      201:
        description: Flight history created successfully
    """
    content = request.get_json()
    flighthistory = FlightHistory.create_from_dto(content)
    flighthistory_controller.create(flighthistory)
    return make_response(jsonify(flighthistory.put_into_dto()), HTTPStatus.CREATED)


@flighthistory_bp.get('/<int:flighthistory_id>')
def get_flighthistory(flighthistory_id: int) -> Response:
    """
    Get flight history by ID
    ---
    tags:
      - Flight History
    parameters:
      - in: path
        name: flighthistory_id
        type: integer
        required: true
        description: Flight history ID
    responses:
      200:
        description: Flight history data
      404:
        description: Flight history not found
    """
    return make_response(jsonify(flighthistory_controller.find_by_id(flighthistory_id)), HTTPStatus.OK)


@flighthistory_bp.put('/<int:flighthistory_id>')
def update_flighthistory(flighthistory_id: int) -> Response:
    """
    Update flight history by ID
    ---
    tags:
      - Flight History
    parameters:
      - in: path
        name: flighthistory_id
        type: integer
        required: true
        description: Flight history ID
      - in: body
        name: flighthistory
        description: Updated flight history data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            actual_departure_time:
              type: string
              format: date-time
              description: Actual departure time
            actual_arrival_time:
              type: string
              format: date-time
              description: Actual arrival time
            status:
              type: string
              description: Flight status
    responses:
      200:
        description: Flight history updated successfully
      404:
        description: Flight history not found
    """
    content = request.get_json()
    flighthistory = FlightHistory.create_from_dto(content)
    flighthistory_controller.update(flighthistory_id, flighthistory)
    return make_response("FlightHistory updated", HTTPStatus.OK)


@flighthistory_bp.patch('/<int:flighthistory_id>')
def patch_flighthistory(flighthistory_id: int) -> Response:
    """
    Partially update flight history by ID
    ---
    tags:
      - Flight History
    parameters:
      - in: path
        name: flighthistory_id
        type: integer
        required: true
        description: Flight history ID
      - in: body
        name: flighthistory
        description: Partial flight history data
        required: true
        schema:
          type: object
          properties:
            flight_id:
              type: integer
              description: Flight ID
            actual_departure_time:
              type: string
              format: date-time
              description: Actual departure time
            actual_arrival_time:
              type: string
              format: date-time
              description: Actual arrival time
            status:
              type: string
              description: Flight status
    responses:
      200:
        description: Flight history updated successfully
      404:
        description: Flight history not found
    """
    content = request.get_json()
    flighthistory_controller.patch(flighthistory_id, content)
    return make_response("FlightHistory updated", HTTPStatus.OK)


@flighthistory_bp.delete('/<int:flighthistory_id>')
def delete_flighthistory(flighthistory_id: int) -> Response:
    """
    Delete flight history by ID
    ---
    tags:
      - Flight History
    parameters:
      - in: path
        name: flighthistory_id
        type: integer
        required: true
        description: Flight history ID
    responses:
      200:
        description: Flight history deleted successfully
      404:
        description: Flight history not found
    """
    flighthistory_controller.delete(flighthistory_id)
    return make_response("FlightHistory deleted", HTTPStatus.OK)


@flighthistory_bp.get('/find-flighthistories-by-flight/<int:flight_id>')
def get_flighthistories_after_flight(flight_id: int) -> Response:
    """
    Find flight histories by flight ID
    ---
    tags:
      - Flight History
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
    responses:
      200:
        description: List of flight histories for the flight
      404:
        description: Flight not found
    """
    return make_response(jsonify(flighthistory_controller.get_flighthistories_after_flight(flight_id)),
                         HTTPStatus.OK)
