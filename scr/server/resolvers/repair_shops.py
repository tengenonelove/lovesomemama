from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import AutoRepairShop


def get(shop_id: int) -> AutoRepairShop | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, city, number, name FROM auto_repair_shop WHERE id=(?)',
        args=(shop_id,))

    return None if not res else AutoRepairShop(
        id=res[0],
        city=res[1],
        number=res[2],
        name=res[3]
    )


def get_all() -> list[AutoRepairShop] | dict:
    shops_list = dbmanager.execute_query(
        query="SELECT id, city, number, name FROM auto_repair_shop",
        fetchone=False)

    res = []

    if shops_list:
        for shop in shops_list:
            res.append(AutoRepairShop(
                id=shop[0],
                city=shop[1],
                number=shop[2],
                name=shop[3]
            ))

    return res


def delete(shop_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM auto_repair_shop WHERE id=(?) RETURNING id',
        args=(shop_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_shop: AutoRepairShop) -> AutoRepairShop | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO auto_repair_shop (city, number, name) VALUES (?, ?, ?) RETURNING id",
        args=(new_shop.city, new_shop.number, new_shop.name))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(shop_id: int, new_data: AutoRepairShop) -> AutoRepairShop | dict:
    res = dbmanager.execute_query(
        query="UPDATE auto_repair_shop SET (city, number, name) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.city, new_data.number, new_data.name, shop_id))

    if type(res) != dict:
        res = get(shop_id)

    return res
