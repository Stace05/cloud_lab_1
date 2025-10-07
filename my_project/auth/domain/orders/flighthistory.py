from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class FlightHistory(db.Model, IDto):

    __tablename__ = "flighthistory"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)
    flight = db.relationship("Flight", backref="flighthistory")
    date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.flight_id}', '{self.date}'"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "date": self.date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> FlightHistory:
        obj = FlightHistory(**dto_dict)
        return obj
