from fastapi import APIRouter, Request, Response, status

from ..models.factionDTO import FactionCreateDTO, FactionUpdateDTO
from ..services.factionsService import FactionService

router = APIRouter(prefix="/factions", tags=["Factions"])

@router.get("/")
async def get_factions(request: Request, response: Response):
    return await FactionService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_faction_by_id(id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).get_by_id(id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return {"error": "Faction not found"}
        
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
            return {"error": "Faction not found"}
        
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
            return {"error": "Faction not found"}
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}