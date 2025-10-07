from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class AirlineAirport(db.Model, IDto):

    __tablename__ = "airlineairport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey("airline.id"), nullable=False)
    airline = db.relationship("Airline", backref="airlineairport")
    airport_id = db.Column(db.Integer, db.ForeignKey("airport.id"), nullable=False)
    airport = db.relationship("Airport", backref="airlineairport")

    def __repr__(self) -> str:
        return f"AirlineAirport({self.id}, '{self.airline_id}', '{self.airport_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "airline_id": self.airline_id,
            "airport_id": self.airport_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AirlineAirport:
        obj = AirlineAirport(**dto_dict)
        return obj
