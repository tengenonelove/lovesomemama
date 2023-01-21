from typing import Optional
from pydantic import BaseModel


class BaseModelModify(BaseModel):
    id: Optional[int]


class Car(BaseModelModify):
    stamp: str
    year_of_release: str
    volume_of_liters: str


class AutoRepairShop(BaseModelModify):
    city: str
    number: str
    name: str


class Staff(BaseModelModify):
    name: str
    surname: str
    patronymic: str
    date: int
    auto_repair_shop_id: int
    post_id: int


class Post(BaseModelModify):
    name_post: str
    master_id: int


class Master(BaseModelModify):
    name_master: str
    service_id: int


class TypeOfServices(BaseModelModify):
    name_services: str
    period_of_execution: str
    cost: int


class User(BaseModelModify):
    login: str
    password: str


class UserReg(User):
    power_level: int
