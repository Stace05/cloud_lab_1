from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import flight_controller
from my_project.auth.domain import Flight

flight_bp = Blueprint('flights', __name__, url_prefix='/flights')


@flight_bp.get('')
def get_all_flights() -> Response:
    """
    Get all flights
    ---
    tags:
      - Flight
    responses:
      200:
        description: List of all flights
    """
    return make_response(jsonify(flight_controller.find_all()), HTTPStatus.OK)


@flight_bp.post('')
def create_flight() -> Response:
    """
    Create new flight
    ---
    tags:
      - Flight
    parameters:
      - in: body
        name: flight
        description: Flight data
        required: true
        schema:
          type: object
          properties:
            flight_number:
              type: string
              description: Flight number
            aircraft_id:
              type: integer
              description: Aircraft ID
            route_id:
              type: integer
              description: Route ID
            departure_time:
              type: string
              format: date-time
              description: Departure time
            arrival_time:
              type: string
              format: date-time
              description: Arrival time
    responses:
      201:
        description: Flight created successfully
    """
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_controller.create(flight)
    return make_response(jsonify(flight.put_into_dto()), HTTPStatus.CREATED)


@flight_bp.get('/<int:flight_id>')
def get_flight(flight_id: int) -> Response:
    """
    Get flight by ID
    ---
    tags:
      - Flight
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
    responses:
      200:
        description: Flight data
      404:
        description: Flight not found
    """
    return make_response(jsonify(flight_controller.find_by_id(flight_id)), HTTPStatus.OK)


@flight_bp.put('/<int:flight_id>')
def update_flight(flight_id: int) -> Response:
    """
    Update flight by ID
    ---
    tags:
      - Flight
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
      - in: body
        name: flight
        description: Updated flight data
        required: true
        schema:
          type: object
          properties:
            flight_number:
              type: string
              description: Flight number
            aircraft_id:
              type: integer
              description: Aircraft ID
            route_id:
              type: integer
              description: Route ID
            departure_time:
              type: string
              format: date-time
              description: Departure time
            arrival_time:
              type: string
              format: date-time
              description: Arrival time
    responses:
      200:
        description: Flight updated successfully
      404:
        description: Flight not found
    """
    content = request.get_json()
    flight = Flight.create_from_dto(content)
    flight_controller.update(flight_id, flight)
    return make_response("Flight updated", HTTPStatus.OK)


@flight_bp.patch('/<int:flight_id>')
def patch_flight(flight_id: int) -> Response:
    """
    Partially update flight by ID
    ---
    tags:
      - Flight
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
      - in: body
        name: flight
        description: Partial flight data
        required: true
        schema:
          type: object
          properties:
            flight_number:
              type: string
              description: Flight number
            aircraft_id:
              type: integer
              description: Aircraft ID
            route_id:
              type: integer
              description: Route ID
            departure_time:
              type: string
              format: date-time
              description: Departure time
            arrival_time:
              type: string
              format: date-time
              description: Arrival time
    responses:
      200:
        description: Flight updated successfully
      404:
        description: Flight not found
    """
    content = request.get_json()
    flight_controller.patch(flight_id, content)
    return make_response("Flight updated", HTTPStatus.OK)


@flight_bp.delete('/<int:flight_id>')
def delete_flight(flight_id: int) -> Response:
    """
    Delete flight by ID
    ---
    tags:
      - Flight
    parameters:
      - in: path
        name: flight_id
        type: integer
        required: true
        description: Flight ID
    responses:
      200:
        description: Flight deleted successfully
      404:
        description: Flight not found
    """
    flight_controller.delete(flight_id)
    return make_response("Flight deleted", HTTPStatus.OK)


@flight_bp.get('/find-flights-by-aircraft/<int:aircraft_id>')
def get_flights_after_aircraft(aircraft_id: int) -> Response:
    """
    Find flights by aircraft ID
    ---
    tags:
      - Flight
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
    responses:
      200:
        description: List of flights for the aircraft
      404:
        description: Aircraft not found
    """
    return make_response(jsonify(flight_controller.get_flights_after_aircraft(aircraft_id)),
                         HTTPStatus.OK)
