from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Registration(db.Model, IDto):

    __tablename__ = "registration"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id"), nullable=False)
    aircraft = db.relationship("Aircraft", backref = "registration")
    registration_date = db.Column(db.DateTime, nullable=False)
    expiry_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return (f"Airline({self.id}, '{self.aircraft_id}', '{self.aircraft}', '{self.registration_date}', "
                f"{self.expiry_date})")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "registration_date": self.registration_date,
            "expiry_date": self.expiry_date
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Registration:
        obj = Registration(**dto_dict)
        return obj
