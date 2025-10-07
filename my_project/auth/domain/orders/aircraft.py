from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Aircraft(db.Model, IDto):

    __tablename__ = "aircraft"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    airline_id = db.Column(db.Integer, db.ForeignKey("airline.id"), nullable=False)
    airline = db.relationship("Airline", backref="aircraft")
    model = db.Column(db.String(45), nullable=False)
    registration_number = db.Column(db.String(20), nullable=False)
    total_flight_hours = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return (f"Airline({self.id}, '{self.airline_id}', '{self.model}', '{self.registration_number}', "
                f"{self.total_flight_hours})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "airline_id": self.airline_id,
            "model": self.model,
            "registration_number": self.registration_number,
            "total_flight_hours": self.total_flight_hours
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Aircraft:
        obj = Aircraft(**dto_dict)
        return obj
