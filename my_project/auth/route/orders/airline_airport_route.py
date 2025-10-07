from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import airline_airport_controller
from my_project.auth.domain import AirlineAirport

airline_airport_bp = Blueprint('airline_airports', __name__, url_prefix='/airline-airports')


@airline_airport_bp.get('')
def get_all_airlines() -> Response:
    """
    Get all airline-airport relationships
    ---
    tags:
      - Airline Airport
    responses:
      200:
        description: List of all airline-airport relationships
    """
    return make_response(jsonify(airline_airport_controller.find_all()), HTTPStatus.OK)


@airline_airport_bp.post('')
def create_airline() -> Response:
    """
    Create new airline-airport relationship
    ---
    tags:
      - Airline Airport
    parameters:
      - in: body
        name: airline_airport
        description: Airline-airport relationship data
        required: true
        schema:
          type: object
          properties:
            airline_id:
              type: integer
              description: Airline ID
            airport_id:
              type: integer
              description: Airport ID
    responses:
      201:
        description: Airline-airport relationship created successfully
    """
    content = request.get_json()
    airline_airport = AirlineAirport.create_from_dto(content)
    airline_airport_controller.create(airline_airport)
    return make_response(jsonify(airline_airport.put_into_dto()), HTTPStatus.CREATED)


@airline_airport_bp.get('/<int:airline_airport_id>')
def get_airline(airline_airport_id: int) -> Response:
    """
    Get airline-airport relationship by ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airline_airport_id
        type: integer
        required: true
        description: Airline-airport relationship ID
    responses:
      200:
        description: Airline-airport relationship data
      404:
        description: Airline-airport relationship not found
    """
    return make_response(jsonify(airline_airport_controller.find_by_id(airline_airport_id)), HTTPStatus.OK)


@airline_airport_bp.put('/<int:airline_airport_id>')
def update_airline(airline_airport_id: int) -> Response:
    """
    Update airline-airport relationship by ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airline_airport_id
        type: integer
        required: true
        description: Airline-airport relationship ID
      - in: body
        name: airline_airport
        description: Updated airline-airport relationship data
        required: true
        schema:
          type: object
          properties:
            airline_id:
              type: integer
              description: Airline ID
            airport_id:
              type: integer
              description: Airport ID
    responses:
      200:
        description: Airline-airport relationship updated successfully
      404:
        description: Airline-airport relationship not found
    """
    content = request.get_json()
    airline_airport = AirlineAirport.create_from_dto(content)
    airline_airport_controller.update(airline_airport_id, airline_airport)
    return make_response("AirlineAirport updated", HTTPStatus.OK)


@airline_airport_bp.patch('/<int:airline_airport_id>')
def patch_airline(airline_airport_id: int) -> Response:
    """
    Partially update airline-airport relationship by ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airline_airport_id
        type: integer
        required: true
        description: Airline-airport relationship ID
      - in: body
        name: airline_airport
        description: Partial airline-airport relationship data
        required: true
        schema:
          type: object
          properties:
            airline_id:
              type: integer
              description: Airline ID
            airport_id:
              type: integer
              description: Airport ID
    responses:
      200:
        description: Airline-airport relationship updated successfully
      404:
        description: Airline-airport relationship not found
    """
    content = request.get_json()
    airline_airport_controller.patch(airline_airport_id, content)
    return make_response("AirlineAirport updated", HTTPStatus.OK)


@airline_airport_bp.delete('/<int:airline_airport_id>')
def delete_airline(airline_airport_id: int) -> Response:
    """
    Delete airline-airport relationship by ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airline_airport_id
        type: integer
        required: true
        description: Airline-airport relationship ID
    responses:
      200:
        description: Airline-airport relationship deleted successfully
      404:
        description: Airline-airport relationship not found
    """
    airline_airport_controller.delete(airline_airport_id)
    return make_response("AirlineAirport deleted", HTTPStatus.OK)


@airline_airport_bp.get('/find-airports-by-airline/<int:airline_id>')
def get_airports_after_airline(airline_id: int) -> Response:
    """
    Find airports by airline ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
    responses:
      200:
        description: List of airports for the airline
      404:
        description: Airline not found
    """
    return make_response(jsonify(airline_airport_controller.get_airports_after_airline(airline_id)),
                         HTTPStatus.OK)


@airline_airport_bp.get('/find-airlines-by-airport/<int:airport_id>')
def get_airlines_after_airport(airport_id: int) -> Response:
    """
    Find airlines by airport ID
    ---
    tags:
      - Airline Airport
    parameters:
      - in: path
        name: airport_id
        type: integer
        required: true
        description: Airport ID
    responses:
      200:
        description: List of airlines for the airport
      404:
        description: Airport not found
    """
    return make_response(jsonify(airline_airport_controller.get_airlines_after_airport(airport_id)),
                         HTTPStatus.OK)