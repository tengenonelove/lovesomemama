from src.server.sql_base.db_manager import dbmanager
from src.server.sql_base.models import TypeOfServices


def get(type_id: int) -> TypeOfServices | None | dict:
    res = dbmanager.execute_query(
        query='SELECT id, name_service, period_of_execution, cost FROM type_of_service WHERE id=(?)',
        args=(type_id,))

    return None if not res else TypeOfServices(
        id=res[0],
        name_service=res[1],
        period_of_execution=res[2],
        cost=res[3]
    )


def get_all() -> list[TypeOfServices] | dict:
    types_list = dbmanager.execute_query(
        query="SELECT id, name_service, period_of_execution, cost FROM type_of_service",
        fetchone=False)

    res = []

    if types_list:
        for type in types_list:
            res.append(TypeOfServices(
                id=type[0],
                name_service=type[1],
                period_of_execution=type[2],
                cost=type[3]
            ))

    return res


def delete(type_id: int) -> int | dict | None:
    res = dbmanager.execute_query(
        query='DELETE FROM type_of_service WHERE id=(?) RETURNING id',
        args=(type_id,))

    if type(res) == tuple:
        return res[0]

    return res


def create(new_shop: TypeOfServices) -> TypeOfServices | dict:
    res = dbmanager.execute_query(
        query="INSERT INTO type_of_service (name_service, period_of_execution, cost) VALUES (?, ?, ?) RETURNING id",
        args=(new_shop.name_services, new_shop.period_of_execution, new_shop.cost))

    if type(res) != dict:
        res = get(res[0])

    return res


def update(type_id: int, new_data: TypeOfServices) -> TypeOfServices | dict:
    res = dbmanager.execute_query(
        query="UPDATE type_of_service SET (name_service, period_of_execution, cost) = (?, ?, ?) WHERE id=(?)",
        args=(new_data.name_services, new_data.period_of_execution, new_data.cost, type_id))

    if type(res) != dict:
        res = get(type_id)

    return res
