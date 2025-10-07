from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Airport(db.Model, IDto):

    __tablename__ = "airport"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    airport_name = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"Airline({self.id}, '{self.airport_name}', '{self.city}', '{self.country}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "airport_name": self.airport_name,
            "city": self.city,
            "country": self.country
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Airport:
        obj = Airport(**dto_dict)
        return obj
