from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import airline_controller
from my_project.auth.domain import Airline

airline_bp = Blueprint('airlines', __name__, url_prefix='/airlines')


@airline_bp.get('')
def get_all_airlines() -> Response:
    """
    Get all airlines
    ---
    tags:
      - Airline
    responses:
      200:
        description: List of all airlines
    """
    return make_response(jsonify(airline_controller.find_all()), HTTPStatus.OK)


@airline_bp.post('')
def create_airline() -> Response:
    """
    Create new airline
    ---
    tags:
      - Airline
    parameters:
      - in: body
        name: airline
        description: Airline data
        required: true
        schema:
          type: object
          properties:
            airline_name:
              type: string
              description: Airline name
            country:
              type: string
              description: Country
            fleet_size:
              type: integer
              description: Fleet size
    responses:
      201:
        description: Airline created successfully
    """
    content = request.get_json()
    airline = Airline.create_from_dto(content)
    airline_controller.create(airline)
    return make_response(jsonify(airline.put_into_dto()), HTTPStatus.CREATED)


@airline_bp.get('/<int:airline_id>')
def get_airline(airline_id: int) -> Response:
    """
    Get airline by ID
    ---
    tags:
      - Airline
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
    responses:
      200:
        description: Airline data
      404:
        description: Airline not found
    """
    return make_response(jsonify(airline_controller.find_by_id(airline_id)), HTTPStatus.OK)


@airline_bp.put('/<int:airline_id>')
def update_airline(airline_id: int) -> Response:
    """
    Update airline by ID
    ---
    tags:
      - Airline
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
      - in: body
        name: airline
        description: Updated airline data
        required: true
        schema:
          type: object
          properties:
            airline_name:
              type: string
              description: Airline name
            country:
              type: string
              description: Country
            fleet_size:
              type: integer
              description: Fleet size
    responses:
      200:
        description: Airline updated successfully
      404:
        description: Airline not found
    """
    content = request.get_json()
    airline = Airline.create_from_dto(content)
    airline_controller.update(airline_id, airline)
    return make_response("Airline updated", HTTPStatus.OK)


@airline_bp.patch('/<int:airline_id>')
def patch_airline(airline_id: int) -> Response:
    """
    Partially update airline by ID
    ---
    tags:
      - Airline
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
      - in: body
        name: airline
        description: Partial airline data
        required: true
        schema:
          type: object
          properties:
            airline_name:
              type: string
              description: Airline name
            country:
              type: string
              description: Country
            fleet_size:
              type: integer
              description: Fleet size
    responses:
      200:
        description: Airline updated successfully
      404:
        description: Airline not found
    """
    content = request.get_json()
    airline_controller.patch(airline_id, content)
    return make_response("Airline updated", HTTPStatus.OK)


@airline_bp.delete('/<int:airline_id>')
def delete_airline(airline_id: int) -> Response:
    """
    Delete airline by ID
    ---
    tags:
      - Airline
    parameters:
      - in: path
        name: airline_id
        type: integer
        required: true
        description: Airline ID
    responses:
      200:
        description: Airline deleted successfully
      404:
        description: Airline not found
    """
    airline_controller.delete(airline_id)
    return make_response("Airline deleted", HTTPStatus.OK)


