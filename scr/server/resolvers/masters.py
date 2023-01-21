from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import Master


def get(master_id: int) -> Master | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, name_master, type_of_service_id FROM master WHERE id=(?)',
        args=(master_id,))

    return None if not res else Master(
        id=res[0],
        name_master=res[1],
        service_id=res[2]
    )


def get_all() -> list[Master] | dict:
    masters_list = dbmanager.execute_query(
        query="SELECT id, name_master, type_of_service_id FROM master",
        fetchone=False)

    res = []

    if masters_list:
        for master in masters_list:
            res.append(Master(
                id=master[0],
                name_master=master[1],
                service_id=master[2]
            ))

    return res


def delete(master_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM master WHERE id=(?) RETURNING id',
        args=(master_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_master: Master) -> Master | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO master (name_master, type_of_service_id) VALUES (?, ?) RETURNING id",
        args=(new_master.name_master, new_master.service_id))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(master_id: int, new_data: Master) -> Master | dict:
    res = dbmanager.execute_query(
        query="UPDATE master SET (type_of_service_id, name_master) = (?, ?) WHERE id=(?)",
        args=(new_data.service_id, new_data.name_master, master_id))

    if type(res) != dict:
        res = get(master_id)

    return res
