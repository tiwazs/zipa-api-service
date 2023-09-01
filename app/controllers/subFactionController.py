from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.subFactionDTO import SubFactionCreateDTO, SubFactionUpdateDTO
from ..services.subFactionService import SubFactionService

router = APIRouter(prefix="/sub_factions", tags=["SubFactions"])

msg_not_found = 'SubFaction not found'

@router.get("/")
async def get_sub_factions(request: Request, response: Response, include_ranks: bool = True, include_units: bool = True):
    return await SubFactionService(request.app.state.db).get_all(include_ranks, include_units)

@router.get("/{id}")
async def get_sub_faction_by_id(id: str, request: Request, response: Response, include_ranks: bool = True, include_units: bool = True):
    try:
        sub_faction = await SubFactionService(request.app.state.db).get_by_id(id, include_ranks, include_units)
        if sub_faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return sub_faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_sub_faction(sub_faction: SubFactionCreateDTO, request: Request, response: Response):
    try:
        return await SubFactionService(request.app.state.db).create(sub_faction)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/update/{id}")
async def update_sub_faction(id: str, sub_faction: SubFactionUpdateDTO, request: Request, response: Response):
    try:
        sub_faction = await SubFactionService(request.app.state.db).update(id, sub_faction)
        if sub_faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return sub_faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.delete("/{id}")
async def delete_sub_faction(id: str, request: Request, response: Response):
    try:
        sub_faction = await SubFactionService(request.app.state.db).delete(id)
        if sub_faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return sub_faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.post("/image/{id}")
async def upload_effect_image(id: str, request: Request, response: Response, image: UploadFile = File(...)):
    try:
        filepath = await SubFactionService(request.app.state.db).upload_image(id, image)
        if filepath is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return filepath
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}    