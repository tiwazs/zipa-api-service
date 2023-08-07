from fastapi import APIRouter, Request, Response, status

from ..models.unitSpecializationDTO import UnitSpecializationCreateDTO, UnitSpecializationItemCreateDTO, UnitSpecializationUpdateDTO
from ..services.unitSpecializationService import UnitSpecializationService

router = APIRouter(prefix="/specializations", tags=["UnitSpecializations"])

msg_not_found = 'Unit Specialization not found'

@router.get("/")
async def get_units(request: Request, response: Response, include_traits: bool = True, include_skills: bool = True, include_items: bool = True):
    return await UnitSpecializationService(request.app.state.db).get_all(include_items, include_skills, include_traits)

@router.get("/faction/{id}")
async def get_units_by_faction_id(id: str, request: Request, response: Response, include_traits: bool = True, include_skills: bool = True, include_items: bool = True):
    try:
        units = await UnitSpecializationService(request.app.state.db).get_by_faction_id(id, include_items, include_skills, include_traits)
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
        unit = await UnitSpecializationService(request.app.state.db).get_by_id(id, include_items, include_skills, include_traits)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_unit(unit: UnitSpecializationCreateDTO, request: Request, response: Response):
    try:
        return await UnitSpecializationService(request.app.state.db).create(unit)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/update/{id}")
async def update_unit(id: str, unit: UnitSpecializationUpdateDTO, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).update(id, unit)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_trait/{id}")
async def add_trait_to_unit(id: str, trait_id: str, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).add_trait(id, trait_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_unit(id: str, trait_id: str, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).remove_trait(id, trait_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_skill/{id}")
async def add_skill_to_unit(id: str, skill_id: str, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).add_skill(id, skill_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_skill/{id}")
async def remove_skill_from_unit(id: str, skill_id: str, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).remove_skill(id, skill_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_item/{id}")
async def add_item_to_unit(id: str, unit_item: UnitSpecializationItemCreateDTO, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).add_item(id, unit_item.item_id, unit_item.quantity)
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
        unit = await UnitSpecializationService(request.app.state.db).remove_item(id, item_id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/update_item/{id}")
async def update_item_from_unit(id: str, unit_item: UnitSpecializationItemCreateDTO, request: Request, response: Response):
    try:
        unit = await UnitSpecializationService(request.app.state.db).update_item(id, unit_item)
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
        unit = await UnitSpecializationService(request.app.state.db).delete(id)
        if unit is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return unit
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}