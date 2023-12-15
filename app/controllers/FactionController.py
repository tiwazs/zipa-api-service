from fastapi import APIRouter, Request, Response, status, File, UploadFile

from ..models.FactionDTO import FactionCreateDTO, FactionMemberDTO, FactionRankCreateDTO, FactionRelationDTO, FactionUpdateDTO
from ..services.FactionService import FactionService

router = APIRouter(prefix="/factions", tags=["Factions"])

msg_not_found = 'Faction not found'

@router.get("/")
async def get_factions(request: Request, response: Response, include_ranks: bool = True, include_units: bool = True,  include_vassal_subjects:bool = False,  include_overlord:bool = False, only_overlords:bool = False):
    return await FactionService(request.app.state.db).get_all(include_ranks, include_units, include_vassal_subjects, include_overlord, only_overlords)

@router.get("/{id}")
async def get_faction_by_id(id: str, request: Request, response: Response, include_ranks: bool = True, include_units: bool = True,  include_vassal_subjects:bool = False,  include_overlord:bool = False):
    try:
        faction = await FactionService(request.app.state.db).get_by_id(id, include_ranks, include_units, include_vassal_subjects, include_overlord)
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
    
@router.put("/update/{id}")
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

@router.put("/add_rank/{id}")
async def add_rank_to_faction(id: str, rank: FactionRankCreateDTO, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).add_rank(rank)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/delete_rank/{id}")
async def remove_rank_from_faction(id: str, rank_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).delete_rank(id, rank_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/add_member/{id}")
async def add_member_to_faction(id: str, member: FactionMemberDTO, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).add_unit(member)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_member/{id}")
async def remove_item_from_unit(id: str, member_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).remove_unit(id, member_id)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_relation")
async def add_member_to_faction(relation: FactionRelationDTO, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).add_relation(relation)
        if faction is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return faction
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_relation")
async def remove_item_from_unit(faction_id: str, faction2_id: str, request: Request, response: Response):
    try:
        faction = await FactionService(request.app.state.db).remove_relation(faction_id, faction2_id)
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