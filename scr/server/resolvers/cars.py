from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Car


def get(car_id: int) -> Car | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, stamp, year_of_release, volume_of_liters FROM cars WHERE id=(?)',
        args=(car_id,))

    return None if not res else Car(
        id=res[0],
        stamp=res[1],
        year_of_release=res[2],
        volume_of_liters=res[3]
    )


def get_all() -> list[Car] | dict:
    cars_list = dbmanager.execute_query(
        query="SELECT id, stamp, year_of_release, volume_of_liters FROM cars",
        fetchone=False)

    res = []

    if cars_list:
        for car in cars_list:
            res.append(Car(
                id=car[0],
                stamp=car[1],
                year_of_release=res[2],
                volume_of_liters=res[3]
            ))

    return res


def delete(car_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM cars WHERE id=(?) RETURNING id',
        args=(car_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_car: Car) -> Car | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO cars (stamp, year_of_release, volume_of_liters) VALUES (?, ?, ?) RETURNING id",
        args=(new_car.stamp, new_car.year_of_release, new_car.volume_of_liters))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(car_id: int, new_data: Car) -> Car | dict:
    res = dbmanager.execute_query(
        query="UPDATE cars SET (stamp, year_of_release, volume_of_liters) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.stamp, new_data.year_of_release, new_data.volume_of_liters, car_id))

    if type(res) != dict:
        res = get(car_id)

    return res
