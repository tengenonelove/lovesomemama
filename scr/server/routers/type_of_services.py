import fastapi
from src.server.resolvers import type_of_services
from src.server.sql_base.models import TypeOfServices

router = fastapi.APIRouter(prefix='/service/type', tags=['TypeOfServices'])


@router.get("/", response_model=str)
def start_page() -> str:
    return "Hello new user!"


@router.get('/get/{service_type_id}', response_model=TypeOfServices | dict)
def get(service_type_id: int) -> TypeOfServices | dict:
    res = type_of_services.get(service_type_id)
    if res is not None or type(res) == dict:
        return res
    else:
        return {"Error": "Not found"}


@router.get('/get_all', response_model=list[TypeOfServices] | dict)
def get_all() -> list[TypeOfServices] | dict:
    return type_of_services.get_all()


@router.delete('/delete/{service_type_id}', response_model=str | dict)
def remove(service_type_id: int) -> str | dict:
    res = type_of_services.delete(service_type_id)
    if type(res) == int:
        return "Deleted"
    elif res is None:
        return "Not found"
    return res


@router.post('/create/', response_model=TypeOfServices | dict)
def create(new_service_type: TypeOfServices) -> TypeOfServices | dict:
    return type_of_services.create(new_service_type)


@router.put("/update/{service_type_id}", response_model=TypeOfServices | dict)
def update(service_type_id: int, new_data: TypeOfServices):
    return type_of_services.update(type_id=service_type_id,
                                   new_data=new_data)
