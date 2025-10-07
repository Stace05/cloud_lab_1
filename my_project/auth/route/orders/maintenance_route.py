from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import maintenance_controller
from my_project.auth.domain import Maintenance

maintenance_bp = Blueprint('maintenances', __name__, url_prefix='/maintenances')


@maintenance_bp.get('')
def get_all_maintenances() -> Response:
    """
    Get all maintenances
    ---
    tags:
      - Maintenance
    responses:
      200:
        description: List of all maintenances
    """
    return make_response(jsonify(maintenance_controller.find_all()), HTTPStatus.OK)


@maintenance_bp.post('')
def create_maintenance() -> Response:
    """
    Create new maintenance
    ---
    tags:
      - Maintenance
    parameters:
      - in: body
        name: maintenance
        description: Maintenance data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            maintenance_date:
              type: string
              format: date
              description: Maintenance date
            description:
              type: string
              description: Maintenance description
    responses:
      201:
        description: Maintenance created successfully
    """
    content = request.get_json()
    maintenance = Maintenance.create_from_dto(content)
    maintenance_controller.create(maintenance)
    return make_response(jsonify(maintenance.put_into_dto()), HTTPStatus.CREATED)


@maintenance_bp.get('/<int:maintenance_id>')
def get_maintenance(maintenance_id: int) -> Response:
    """
    Get maintenance by ID
    ---
    tags:
      - Maintenance
    parameters:
      - in: path
        name: maintenance_id
        type: integer
        required: true
        description: Maintenance ID
    responses:
      200:
        description: Maintenance data
      404:
        description: Maintenance not found
    """
    return make_response(jsonify(maintenance_controller.find_by_id(maintenance_id)), HTTPStatus.OK)


@maintenance_bp.put('/<int:maintenance_id>')
def update_maintenance(maintenance_id: int) -> Response:
    """
    Update maintenance by ID
    ---
    tags:
      - Maintenance
    parameters:
      - in: path
        name: maintenance_id
        type: integer
        required: true
        description: Maintenance ID
      - in: body
        name: maintenance
        description: Updated maintenance data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            maintenance_date:
              type: string
              format: date
              description: Maintenance date
            description:
              type: string
              description: Maintenance description
    responses:
      200:
        description: Maintenance updated successfully
      404:
        description: Maintenance not found
    """
    content = request.get_json()
    maintenance = Maintenance.create_from_dto(content)
    maintenance_controller.update(maintenance_id, maintenance)
    return make_response("Maintenance updated", HTTPStatus.OK)


@maintenance_bp.patch('/<int:maintenance_id>')
def patch_maintenance(maintenance_id: int) -> Response:
    """
    Partially update maintenance by ID
    ---
    tags:
      - Maintenance
    parameters:
      - in: path
        name: maintenance_id
        type: integer
        required: true
        description: Maintenance ID
      - in: body
        name: maintenance
        description: Partial maintenance data
        required: true
        schema:
          type: object
          properties:
            aircraft_id:
              type: integer
              description: Aircraft ID
            maintenance_date:
              type: string
              format: date
              description: Maintenance date
            description:
              type: string
              description: Maintenance description
    responses:
      200:
        description: Maintenance updated successfully
      404:
        description: Maintenance not found
    """
    content = request.get_json()
    maintenance_controller.patch(maintenance_id, content)
    return make_response("Maintenance updated", HTTPStatus.OK)


@maintenance_bp.delete('/<int:maintenance_id>')
def delete_maintenance(maintenance_id: int) -> Response:
    """
    Delete maintenance by ID
    ---
    tags:
      - Maintenance
    parameters:
      - in: path
        name: maintenance_id
        type: integer
        required: true
        description: Maintenance ID
    responses:
      200:
        description: Maintenance deleted successfully
      404:
        description: Maintenance not found
    """
    maintenance_controller.delete(maintenance_id)
    return make_response("Maintenance deleted", HTTPStatus.OK)


@maintenance_bp.get('/find-maintenances-by-aircraft/<int:aircraft_id>')
def get_maintenances_after_aircraft(aircraft_id: int) -> Response:
    """
    Find maintenances by aircraft ID
    ---
    tags:
      - Maintenance
    parameters:
      - in: path
        name: aircraft_id
        type: integer
        required: true
        description: Aircraft ID
    responses:
      200:
        description: List of maintenances for the aircraft
      404:
        description: Aircraft not found
    """
    return make_response(jsonify(maintenance_controller.get_maintenances_after_aircraft(aircraft_id)),
                         HTTPStatus.OK)
