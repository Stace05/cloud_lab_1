from __future__ import annotations
from typing import Dict, Any

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Flight(db.Model, IDto):

    __tablename__ = "flight"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    aircraft_id = db.Column(db.Integer, db.ForeignKey("aircraft.id"), nullable=False)
    aircraft = db.relationship("Aircraft", backref = "flight")
    route_id = db.Column(db.Integer, db.ForeignKey("route.id"), nullable=False)
    route = db.relationship("Route", backref = "flight")
    departure_time = db.Column(db.DateTime, nullable=False)
    arrival_time = db.Column(db.DateTime, nullable=False)
    speed = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return (f"Airline({self.id}, '{self.aircraft_id}', '{self.aircraft}', '{self.route_id}', "
                f"{self.departure_time}), '{self.arrival_time}', '{self.speed}')")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "aircraft_id": self.aircraft_id,
            "route_id": self.route_id,
            "departure_time": self.departure_time,
            "arrival_time": self.arrival_time,
            "speed": self.speed
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Flight:
        obj = Flight(**dto_dict)
        return obj
