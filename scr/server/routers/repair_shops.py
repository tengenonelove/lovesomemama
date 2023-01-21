import fastapi
from src.server.resolvers import repair_shops
from src.server.sql_base.models import AutoRepairShop

router = fastapi.APIRouter(prefix='/shops', tags=['RepairShops'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{shop_id}', response_model=AutoRepairShop | dict)
def get(shop_id: int) -> AutoRepairShop | dict:
    res = repair_shops.get(shop_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[AutoRepairShop] | dict)
def get_all() -> list[AutoRepairShop] | dict:
    return repair_shops.get_all()


@router.delete('/delete/{shop_id}', response_model=str | dict)
def remove(shop_id: int) -> str | dict:
    res = repair_shops.delete(shop_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=AutoRepairShop | dict)
def create(new_shop: AutoRepairShop) -> AutoRepairShop | dict:
    return repair_shops.create(new_shop)


@router.put("/update/{shop_id}", response_model=AutoRepairShop | dict)
def update(shop_id: int, new_data: AutoRepairShop):
    return repair_shops.update(shop_id=shop_id,
                               new_data=new_data)
