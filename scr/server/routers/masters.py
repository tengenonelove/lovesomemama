import fastapi
from src.server.resolvers import masters
from src.server.sql_base.models import Master

router = fastapi.APIRouter(prefix='/master', tags=['Masters'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{master_id}', response_model=Master | dict)
def get(master_id: int) -> Master | dict:
    res = masters.get(master_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[Master] | dict)
def get_all() -> list[Master] | dict:
    return masters.get_all()


@router.delete('/delete/{master_id}', response_model=str | dict)
def remove(master_id: int) -> str | dict:
    res = masters.delete(master_id)
    if type(res) == int:
        return {"code": 200, "message": "Deleted"}
    elif res is None:
        return {"code": 400, "message": "Not found"}
    else:
        return {"code": 400, "message": "Error"}


@router.post('/create/', response_model=dict)
def create(new_master: Master) -> dict:
    master = masters.create(new_master)
    if type(master) != dict:
        return {"code": 200, "message": "Successfully", "master": master}
    else:
        return {"code": 400, "message": "Error", "master": None}


@router.put("/update/{master_id}", response_model=Master | dict)
def update(master_id: int, new_data: Master):
    master = masters.update(master_id=master_id,
                            new_data=new_data)
    if type(master) == Master:
        return {"code": 200, "message": "Successfully", "master": master}
    else:
        return {"code": 400, "message": "Error", "master": None}

