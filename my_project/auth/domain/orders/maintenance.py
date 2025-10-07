from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Maintenance(db.Model, IDto):

    __tablename__ = "maintenance"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id"), nullable=False)
    aircraft = db.relationship("Aircraft", backref = "maintenance")
    date = db.Column(db.DateTime, nullable=False)
    details = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.aircraft_id}', '{self.aircraft}', '{self.date}', {self.details})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "date": self.date,
            "details": self.details,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Maintenance:
        obj = Maintenance(**dto_dict)
        return obj
