from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Staff


def get(staff_id: int) -> Staff | None | dict:
    res = dbmanager.execute_query(
        query='SELECT name, surname, patronymic, date, auto_repair_shop_id, post_id FROM staff WHERE id=(?)',
        args=(staff_id,))

    return None if not res else Staff(
        id=res[0],
        name=res[1],
        surname=res[2],
        patronymic=res[3],
        date=res[4],
        auto_repair_shop_id=res[5],
        post_id=res[6]
    )


def get_all() -> list[Staff] | dict:
    staff_list = dbmanager.execute_query(
        query="SELECT id, name, surname, patronymic, date, auto_repair_shop_id, post_id FROM staff",
        fetchone=False)

    res = []

    if staff_list:
        for staff in staff_list:
            res.append(Staff(
                id=staff[0],
                name=staff[1],
                surname=staff[2],
                patronymic=staff[3],
                date=staff[4],
                auto_repair_shop_id=staff[5],
                post_id=staff[6]
            ))

    return res


def delete(staff_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM staff WHERE id=(?) RETURNING id',
        args=(staff_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_shop: Staff) -> Staff | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO staff (name, surname, patronymic, date, auto_repair_shop_id, post_id) VALUES (?, ?, ?, ?, ?, ?) RETURNING id",
        args=(new_shop.name, new_shop.surname, new_shop.patronymic, new_shop.date, new_shop.auto_repair_shop_id,
              new_shop.post_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(staff_id: int, new_data: Staff) -> Staff | dict:
    res = dbmanager.execute_query(
        query="UPDATE staff SET (name, surname, patronymic, date, auto_repair_shop_id, post_id) = (?, ?, ?, ?, ?, ?) WHERE id=(?)",
        args=(new_data.name, new_data.surname, new_data.patronymic, new_data.date, new_data.auto_repair_shop_id,
              new_data.post_id, staff_id))

    if type(res) != dict:
        res = get(staff_id)

    return res
