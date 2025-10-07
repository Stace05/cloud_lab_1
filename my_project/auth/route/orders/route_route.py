from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from my_project.auth.controller import route_controller
from my_project.auth.domain import Route

route_bp = Blueprint('routes', __name__, url_prefix='/routes')


@route_bp.get('')
def get_all_routes() -> Response:
    """
    Get all routes
    ---
    tags:
      - Route
    responses:
      200:
        description: List of all routes
    """
    return make_response(jsonify(route_controller.find_all()), HTTPStatus.OK)


@route_bp.post('')
def create_route() -> Response:
    """
    Create new route
    ---
    tags:
      - Route
    parameters:
      - in: body
        name: route
        description: Route data
        required: true
        schema:
          type: object
          properties:
            departure_airport_id:
              type: integer
              description: Departure airport ID
            arrival_airport_id:
              type: integer
              description: Arrival airport ID
            distance:
              type: number
              format: float
              description: Distance in kilometers
    responses:
      201:
        description: Route created successfully
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.create(route)
    return make_response(jsonify(route.put_into_dto()), HTTPStatus.CREATED)


@route_bp.get('/<int:route_id>')
def get_route(route_id: int) -> Response:
    """
    Get route by ID
    ---
    tags:
      - Route
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: Route data
      404:
        description: Route not found
    """
    return make_response(jsonify(route_controller.find_by_id(route_id)), HTTPStatus.OK)


@route_bp.put('/<int:route_id>')
def update_route(route_id: int) -> Response:
    """
    Update route by ID
    ---
    tags:
      - Route
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
      - in: body
        name: route
        description: Updated route data
        required: true
        schema:
          type: object
          properties:
            departure_airport_id:
              type: integer
              description: Departure airport ID
            arrival_airport_id:
              type: integer
              description: Arrival airport ID
            distance:
              type: number
              format: float
              description: Distance in kilometers
    responses:
      200:
        description: Route updated successfully
      404:
        description: Route not found
    """
    content = request.get_json()
    route = Route.create_from_dto(content)
    route_controller.update(route_id, route)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.patch('/<int:route_id>')
def patch_route(route_id: int) -> Response:
    """
    Partially update route by ID
    ---
    tags:
      - Route
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
      - in: body
        name: route
        description: Partial route data
        required: true
        schema:
          type: object
          properties:
            departure_airport_id:
              type: integer
              description: Departure airport ID
            arrival_airport_id:
              type: integer
              description: Arrival airport ID
            distance:
              type: number
              format: float
              description: Distance in kilometers
    responses:
      200:
        description: Route updated successfully
      404:
        description: Route not found
    """
    content = request.get_json()
    route_controller.patch(route_id, content)
    return make_response("Route updated", HTTPStatus.OK)


@route_bp.delete('/<int:route_id>')
def delete_route(route_id: int) -> Response:
    """
    Delete route by ID
    ---
    tags:
      - Route
    parameters:
      - in: path
        name: route_id
        type: integer
        required: true
        description: Route ID
    responses:
      200:
        description: Route deleted successfully
      404:
        description: Route not found
    """
    route_controller.delete(route_id)
    return make_response("Route deleted", HTTPStatus.OK)


