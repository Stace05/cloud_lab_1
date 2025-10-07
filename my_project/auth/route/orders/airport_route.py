from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import airport_controller
from my_project.auth.domain import Airport

airport_bp = Blueprint('airports', __name__, url_prefix='/airports')


@airport_bp.get('')
def get_all_airports() -> Response:
    """
    Get all airports
    ---
    tags:
      - Airport
    responses:
      200:
        description: List of all airports
    """
    return make_response(jsonify(airport_controller.find_all()), HTTPStatus.OK)


@airport_bp.post('')
def create_airport() -> Response:
    """
    Create new airport
    ---
    tags:
      - Airport
    parameters:
      - in: body
        name: airport
        description: Airport data
        required: true
        schema:
          type: object
          properties:
            airport_name:
              type: string
              description: Airport name
            city:
              type: string
              description: City
            country:
              type: string
              description: Country
    responses:
      201:
        description: Airport created successfully
    """
    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_controller.create(airport)
    return make_response(jsonify(airport.put_into_dto()), HTTPStatus.CREATED)


@airport_bp.get('/<int:airport_id>')
def get_airport(airport_id: int) -> Response:
    """
    Get airport by ID
    ---
    tags:
      - Airport
    parameters:
      - in: path
        name: airport_id
        type: integer
        required: true
        description: Airport ID
    responses:
      200:
        description: Airport data
      404:
        description: Airport not found
    """
    return make_response(jsonify(airport_controller.find_by_id(airport_id)), HTTPStatus.OK)


@airport_bp.put('/<int:airport_id>')
def update_airport(airport_id: int) -> Response:
    """
    Update airport by ID
    ---
    tags:
      - Airport
    parameters:
      - in: path
        name: airport_id
        type: integer
        required: true
        description: Airport ID
      - in: body
        name: airport
        description: Updated airport data
        required: true
        schema:
          type: object
          properties:
            airport_name:
              type: string
              description: Airport name
            city:
              type: string
              description: City
            country:
              type: string
              description: Country
    responses:
      200:
        description: Airport updated successfully
      404:
        description: Airport not found
    """
    content = request.get_json()
    airport = Airport.create_from_dto(content)
    airport_controller.update(airport_id, airport)
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.patch('/<int:airport_id>')
def patch_airport(airport_id: int) -> Response:
    """
    Partially update airport by ID
    ---
    tags:
      - Airport
    parameters:
      - in: path
        name: airport_id
        type: integer
        required: true
        description: Airport ID
      - in: body
        name: airport
        description: Partial airport data
        required: true
        schema:
          type: object
          properties:
            airport_name:
              type: string
              description: Airport name
            city:
              type: string
              description: City
            country:
              type: string
              description: Country
    responses:
      200:
        description: Airport updated successfully
      404:
        description: Airport not found
    """
    content = request.get_json()
    airport_controller.patch(airport_id, content)
    return make_response("Airport updated", HTTPStatus.OK)


@airport_bp.delete('/<int:airport_id>')
def delete_airport(airport_id: int) -> Response:
    """
    Delete airport by ID
    ---
    tags:
      - Airport
    parameters:
      - in: path
        name: airport_id
        type: integer
        required: true
        description: Airport ID
    responses:
      200:
        description: Airport deleted successfully
      404:
        description: Airport not found
    """
    airport_controller.delete(airport_id)
    return make_response("Airport deleted", HTTPStatus.OK)


