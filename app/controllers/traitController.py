from fastapi import APIRouter, Request, Response, status

from ..models.traitDTO import TraitDTO, TraitUpdateDTO, TraitCreateDTO
from ..services.traitService import TraitService

router = APIRouter(prefix="/traits", tags=["Traits"])

msg_not_found = 'Trait not found'

@router.get("/")
async def get_traits(request: Request, response: Response, include_effects: bool = True):
    if include_effects:
        return await TraitService(request.app.state.db).get_all_ext()
    else:
        return await TraitService(request.app.state.db).get_all()

@router.get("/{id}")
async def get_trait_by_id(id: str, request: Request, response: Response, include_effects: bool = True):
    try:
        if include_effects:
            trait = await TraitService(request.app.state.db).get_by_id_ext(id)
        else:
            trait = await TraitService(request.app.state.db).get_by_id(id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.post("/")
async def create_trait(trait: TraitCreateDTO, request: Request, response: Response):
    try:
        return await TraitService(request.app.state.db).create(trait)
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
    
@router.put("/{id}")
async def update_trait(id: str, trait: TraitUpdateDTO, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).update(id, trait)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/add_effect/{id}")
async def add_effect_to_trait(id: str, effect_id: str, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).add_effect(id, effect_id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}

@router.put("/remove_effect/{id}")
async def remove_effect_from_trait(id: str, effect_id: str, request: Request, response: Response):
        trait = await TraitService(request.app.state.db).remove_effect(id, effect_id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait

    
@router.delete("/{id}")
async def delete_trait(id: str, request: Request, response: Response):
    try:
        trait = await TraitService(request.app.state.db).delete(id)
        if trait is None:
            response.status_code = status.HTTP_204_NO_CONTENT
            return { "error" : msg_not_found }
        
        return trait
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}