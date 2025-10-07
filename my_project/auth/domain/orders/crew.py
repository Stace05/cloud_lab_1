from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Crew(db.Model, IDto):

    __tablename__ = "crew"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)
    flight = db.relationship("Flight", backref="crew")
    pilot_id = db.Column(db.Integer, db.ForeignKey("pilot.id"), nullable=False)
    pilot = db.relationship("Pilot", backref="crew")
    role = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.flight_id}', '{self.pilot_id}', '{self.role}'"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "flight_id": self.flight_id,
            "pilot_id": self.pilot_id,
            "role": self.role,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Crew:
        obj = Crew(**dto_dict)
        return obj
