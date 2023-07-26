from fastapi import APIRouter, Request, Response, status

from ..models.unitDTO import UnitDTO,UnitCreateDTO, UnitUpdateDTO
from ..services.unitService import UnitService

router = APIRouter(prefix="/units", tags=["Units"])

msg_not_found = 'Unit not found'

@router.get("/")
async def get_units(request: Request, response: Response, include_traits: bool = True, include_skills: bool = True, include_items: bool = True):
    return await UnitService(request.app.state.db).get_all(include_items, include_skills, include_traits)

@router.get("/faction/{id}")
async def get_units_by_faction_id(id: str, request: Request, response: Response, include_traits: bool = True, include_skills: bool = True, include_items: bool = True):
    try:
        units = await UnitService(request.app.state.db).get_by_faction_id(id, include_items, include_skills, include_traits)
        if units is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return units
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.get("/{id}")
async def get_unit_by_id(id: str, request: Request, response: Response, include_traits: bool = True, include_skills: bool = True, include_items: bool = True):
    try:
        unit = await UnitService(request.app.state.db).get_by_id(id, include_items, include_skills, include_traits)
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
    
@router.put("/{id}")
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