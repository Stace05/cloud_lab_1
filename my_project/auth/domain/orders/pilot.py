from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Pilot(db.Model, IDto):

    __tablename__ = "pilot"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    pilot_name = db.Column(db.String(100), nullable=False)
    pilot_surname = db.Column(db.String(100), nullable=False)
    license_number = db.Column(db.String(50), nullable=False)
    total_flight_hours = db.Column(db.Integer, nullable=False)


    def __repr__(self) -> str:
        return (f"Pilot({self.id}, '{self.pilot_name}', '{self.pilot_surname}', '{self.license_number}', "
                f"'{self.total_flight_hours}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "pilot_name": self.pilot_name,
            "pilot_surname": self.pilot_surname,
            "license_number": self.license_number,
            "total_flight_hours": self.total_flight_hours
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Pilot:
        obj = Pilot(**dto_dict)
        return obj
