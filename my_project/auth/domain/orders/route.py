from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Route(db.Model, IDto):

    __tablename__ = "route"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    departure_airport_id = db.Column(db.Integer, db.ForeignKey("airport.id"), nullable=False)
    departure_airport = db.relationship("Airport", foreign_keys=[departure_airport_id], backref="departure_routes")
    arrival_airport_id = db.Column(db.Integer, db.ForeignKey("airport.id"), nullable=False)
    arrival_airport = db.relationship("Airport", foreign_keys=[arrival_airport_id], backref="arrival_routes")
    distance = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.departure_airport_id}', '{self.arrival_airport_id}', '{self.distance}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "departure_airport_id": self.departure_airport_id,
            "arrival_airport_id": self.arrival_airport_id,
            "distance": self.distance,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Route:
        obj = Route(**dto_dict)
        return obj
