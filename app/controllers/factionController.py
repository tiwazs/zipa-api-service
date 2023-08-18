from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.factionDTO import FactionCreateDTO, FactionUpdateDTO
from ..services.factionService import FactionService

router = APIRouter(prefix="/factions", tags=["Factions"])

msg_not_found = 'Faction not found'

@router.get("/")
async def get_factions(request: Request, response: Response, include_units: bool = False):
    return await FactionService(request.app.state.db).get_all(include_units)

@router.get("/{id}")
async def get_faction_by_id(id: str, request: Request, response: Response, include_units: bool = False):
    try:
        faction = await FactionService(request.app.state.db).get_by_id(id, include_units)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/")
async def create_faction(faction: FactionCreateDTO, request: Request, response: Response):
    try:
        return await FactionService(request.app.state.db).create(faction)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_faction(id: str, faction: FactionUpdateDTO, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).update(id, faction)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_trait/{id}")
async def add_trait_to_faction(id: str, trait_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).add_trait(id, trait_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_trait/{id}")
async def remove_trait_from_faction(id: str, trait_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).remove_trait(id, trait_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_unit/{id}")
async def add_unit_to_faction(id: str, unit_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).add_unit(id, unit_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/remove_unit/{id}")
async def remove_unit_from_faction(id: str, unit_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).remove_unit(id, unit_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_faction(id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).delete(id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await FactionService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)} 