from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import registration_controller
from my_project.auth.domain import Registration

registration_bp = Blueprint('registrations', __name__, url_prefix='/registrations')


@registration_bp.get('')
def get_all_registrations() -> Response:
    """
    Get all registrations
    ---
    tags:
      - Registration
    responses:
      200:
        description: List of all registrations
    """
    return make_response(jsonify(registration_controller.find_all()), HTTPStatus.OK)


@registration_bp.post('')
def create_registration() -> Response:
    """
    Create new registration
    ---
    tags:
      - Registration
    parameters:
      - in: body
        name: registration
        description: Registration data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            registration_number:
              type: string
              description: Registration number
            registration_date:
              type: string
              format: date
              description: Registration date
    responses:
      201:
        description: Registration created successfully
    """
    content = request.get_json()
    registration = Registration.create_from_dto(content)
    registration_controller.create(registration)
    return make_response(jsonify(registration.put_into_dto()), HTTPStatus.CREATED)


@registration_bp.get('/<int:registration_id>')
def get_registration(registration_id: int) -> Response:
    """
    Get registration by ID
    ---
    tags:
      - Registration
    parameters:
      - in: path
        name: registration_id
        type: integer
        required: true
        description: Registration ID
    responses:
      200:
        description: Registration data
      404:
        description: Registration not found
    """
    return make_response(jsonify(registration_controller.find_by_id(registration_id)), HTTPStatus.OK)


@registration_bp.put('/<int:registration_id>')
def update_registration(registration_id: int) -> Response:
    """
    Update registration by ID
    ---
    tags:
      - Registration
    parameters:
      - in: path
        name: registration_id
        type: integer
        required: true
        description: Registration ID
      - in: body
        name: registration
        description: Updated registration data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            registration_number:
              type: string
              description: Registration number
            registration_date:
              type: string
              format: date
              description: Registration date
    responses:
      200:
        description: Registration updated successfully
      404:
        description: Registration not found
    """
    content = request.get_json()
    registration = Registration.create_from_dto(content)
    registration_controller.update(registration_id, registration)
    return make_response("Registration updated", HTTPStatus.OK)


@registration_bp.patch('/<int:registration_id>')
def patch_registration(registration_id: int) -> Response:
    """
    Partially update registration by ID
    ---
    tags:
      - Registration
    parameters:
      - in: path
        name: registration_id
        type: integer
        required: true
        description: Registration ID
      - in: body
        name: registration
        description: Partial registration data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            registration_number:
              type: string
              description: Registration number
            registration_date:
              type: string
              format: date
              description: Registration date
    responses:
      200:
        description: Registration updated successfully
      404:
        description: Registration not found
    """
    content = request.get_json()
    registration_controller.patch(registration_id, content)
    return make_response("Registration updated", HTTPStatus.OK)


@registration_bp.delete('/<int:registration_id>')
def delete_registration(registration_id: int) -> Response:
    """
    Delete registration by ID
    ---
    tags:
      - Registration
    parameters:
      - in: path
        name: registration_id
        type: integer
        required: true
        description: Registration ID
    responses:
      200:
        description: Registration deleted successfully
      404:
        description: Registration not found
    """
    registration_controller.delete(registration_id)
    return make_response("Registration deleted", HTTPStatus.OK)


@registration_bp.get('/find-registrations-by-aircraft/<int:aircraft_id>')
def get_registrations_after_aircraft(aircraft_id: int) -> Response:
    """
    Find registrations by aircraft ID
    ---
    tags:
      - Registration
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
    responses:
      200:
        description: List of registrations for the aircraft
      404:
        description: Aircraft not found
    """
    return make_response(jsonify(registration_controller.get_registrations_after_aircraft(aircraft_id)),
                         HTTPStatus.OK)
