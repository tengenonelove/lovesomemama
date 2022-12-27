from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class cars(BaseModel):
    id: Optional[int]
    stamp: str
    year_of_release: str
    volume_of_liters: str


class auto_repair_shop(BaseModel):
    id: Optional[int]
    city: int
    number: str
    name: str


class staff(BaseModel):
    id: Optional[int]
    name_type: str
    surname: str
    patronomyc: str
    date: int
    auto_repair_shop: str


class post(BaseModel):
    id: Optional[int]
    name_post: str


class master(BaseModel):
    id: Optional[int]
    name_master: str


class type_of_services(BaseModel):
    id: Optional[int]
    name_services: str
    period_of_execution: str
    cost: str



