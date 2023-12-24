from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.unitDTO import UnitCreateDTO, UnitItemCreateDTO, UnitUpdateDTO
from ..services.unitService import UnitService

router = APIRouter(prefix="/units", tags=["Units"])

msg_not_found = 'Unit not found'

@router.get("/normal")
async def get_units(request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    return await UnitService(request.app.state.db).get_all(include_items, include_race, include_specialization)

@router.get("/extended")
async def get_units(request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    return await UnitService(request.app.state.db).get_all_extended(include_items, include_race, include_specialization)

@router.get("/user/normal/{user_id}")
async def get_units_by_user(user_id: str, request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    return await UnitService(request.app.state.db).get_all_by_user(user_id, include_items, include_race, include_specialization)

@router.get("/user/extended/{user_id}")
async def get_units_by_user(user_id: str, request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    return await UnitService(request.app.state.db).get_all_extended_by_user(user_id, include_items, include_race, include_specialization)

@router.get("/normal/{id}")
async def get_unit_by_id(id: str, request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    try:
        unit = await UnitService(request.app.state.db).get_by_id(id, include_items, include_race, include_specialization)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.get("/extended/{id}")
async def get_unit_by_id(id: str, request: Request, response: Response, include_items: bool = True, include_race: bool = True, include_specialization: bool = True):
    try:
        unit = await UnitService(request.app.state.db).get_extended_by_id(id, include_items, include_race, include_specialization)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_unit(unit: UnitCreateDTO, request: Request, response: Response):
    try:
        return await UnitService(request.app.state.db).create(unit)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/update/{id}")
async def update_unit(id: str, unit: UnitUpdateDTO, request: Request, response: Response):
    try:
        unit = await UnitService(request.app.state.db).update(id, unit)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_item/{id}")
async def add_item_to_unit(id: str, unit_item: UnitItemCreateDTO, request: Request, response: Response):
    try:
        unit = await UnitService(request.app.state.db).add_item(id, unit_item.item_id, unit_item.quantity)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_item/{id}")
async def remove_item_from_unit(id: str, item_id: str, request: Request, response: Response):
    try:
        unit = await UnitService(request.app.state.db).remove_item(id, item_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/update_item/{id}")
async def update_item_from_unit(id: str, unit_item: UnitItemCreateDTO, request: Request, response: Response):
    try:
        unit = await UnitService(request.app.state.db).update_item(id, unit_item)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_unit(id: str, request: Request, response: Response):
    try:
        unit = await UnitService(request.app.state.db).delete(id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await UnitService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}    