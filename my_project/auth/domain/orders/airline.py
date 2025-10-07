from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Airline(db.Model, IDto):

    __tablename__ = "airline"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    airline_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    fleet_size = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.airline_name}', '{self.country}', '{self.fleet_size}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "airline_name": self.airline_name,
            "country": self.country,
            "fleet_size": self.fleet_size,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airline:
        obj = Airline(**dto_dict)
        return obj
